import requests,time
from bs4 import BeautifulSoup

#多页爬取，使用列表解析式
urls=['https://www.tripadvisor.cn/Attractions-g293920-Activities-oa{}-Phuket.html#FILTERED_LIST'.format(str(i)) for i in range(30,300,30)]
headers={
    'Uesr-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
    'Cookie''TART=%1%enc%3AjW0HXjEm1ItwS1dmqyU%2F5PVah5dShQAuFHBHE3SwpQOGJAxOJ5AKEUAJfWrgzvdXHOeumsAAzB8%3D; TAUnique=%1%enc%3A%2FXkmY5is6zgb7v0wba0XjGjm1WJ9J3hxL4CTvY3ZIEnLH0eO5X1%2BTQ%3D%3D; TASSK=enc%3AAPf1%2BvGENmhJWfXumZXCQRewDnXj1gNVcEqRXGeTl3ceDGxZAw8FtRzg3IL8MrYpA0wRJVgs4RsrHSiZG78GLj4dhL9pzD6yPgNH%2FS0UYIxgkZJOdkX0FWbPULmJYcW5Aw%3D%3D; TAPD=tripadvisor.cn; _ga=GA1.2.710617404.1544354604; _gid=GA1.2.1867117835.1544354604; SRT=%1%enc%3AjW0HXjEm1ItwS1dmqyU%2F5PVah5dShQAuFHBHE3SwpQOGJAxOJ5AKEUAJfWrgzvdXHOeumsAAzB8%3D; _smt_uid=5c0cfb34.3179dc2e; __gads=ID=018a15f114b48f07:T=1544354613:S=ALNI_MacK3cje0v_hTXSVIv75ku6puStMQ; SecureLogin2=3.4%3AALC1gkoZzrFXuZ12XWNVdpfhN98eHShgnL3BMNUsJ2asVXvWDOgmJG5eozpxgWaQGY%2Fuqsu7uzMImLVTl%2F3xOMkW%2FZGGwZeXeeV3r9PfEBPmJHNBvCU1oIjefoaDp8CZELWL44DqykUqcKXgciW6m7qssjiSBC7iNai9vSrsUliLjcx1okiPt0Z0COgtcqihw5nRfzkEFY0eKvCtOH616AA%3D; TAAuth3=3%3A2f5bed8fd24fdce7ba9e28addfe38577%3AAHXrG5OHEG4lViwC%2B7w6xz5uuXjOfHrw%2Bxt4zNiY9U9U6B%2BXJaFEJIrOE0rf9%2BDNIeCRyhv8DlZm4GRid0PrppyqhzGGYuBcTrLUMW0Te3ENjEv5UPxzsPP5qcwCfG9n2nanySDIzIupxNCVn%2Foc4nQLMZyXgeKlLuRqsFHIciGDvq8rb8nlW8cdOr5Wfg1GZA%3D%3D; CommercePopunder=SuppressAll*1544354761875; CM=%1%PremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CRestAds%2FRPers%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C4%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CRestPartSess%2C%2C-1%7CUVOwnersSess%2C%2C-1%7CCCUVOwnPers%2C%2C-1%7CRestPremRSess%2C%2C-1%7CCCSess%2C%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CRestAdsPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CTADORSess%2C%2C-1%7CAdsRetPers%2C%2C-1%7CTARSWBPers%2C%2C-1%7CSPMCSess%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CSPMCWBPers%2C%2C-1%7CRBAPers%2C%2C-1%7CRestAds%2FRSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7CRestPartPers%2C%2C-1%7CRestPremRPers%2C%2C-1%7CCCUVOwnSess%2C%2C-1%7CUVOwnersPers%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCCPers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CSPMCPers%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CAdsRetSess%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CTADORPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CTARSWBSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7CSPORPers%2C%2C-1%7Cperssticker%2C%2C-1%7CSPMCWBSess%2C%2C-1%7C; BEPIN=%1%16792c29a07%3Busr03t.daodao.com%3A10023%3B; TATravelInfo=V2*AY.2018*AM.12*AD.23*DY.2018*DM.12*DD.24*A.2*MG.-1*HP.2*FL.3*DSM.1544355486504*RS.1; TAReturnTo=%1%%2FHotel_Review-g1379324-d1026083-Reviews-Ayara_Kamala_Resort_Spa-Kamala_Kathu_Phuket.html; roybatty=TNI1625!ANLKvaPs%2FGOsNOsI%2FY5KpCfswHL3J6efUxw0gzz%2Bkk56e%2B5Y%2BXvVnuseer1rAA8fGk3UvIKp7So8HPi2AukoO418ywr8qFvrMwCetWolw68mUIDjKwKgp6SNVta79%2FoKlsSn%2FoDjCZm0c%2FteCnvfHbEyVf%2B2AiOAVpebNOVWtctc%2C1; TASession=%1%V2ID.91619124196ED28C5083A64769F5B0F1*SQ.62*LP.%2FLangRedirect%3Fauto%3D3%26origin%3Dzh%26pool%3DX%26returnTo%3D%252F*LS.DemandLoadAjax*GR.41*TCPAR.84*TBR.5*EXEX.92*ABTR.46*PHTB.65*FS.4*CPU.95*HS.recommended*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.567EEFC6F8150A7DD5B9621F77FF0EFA*LF.zhCN*FA.1*DF.0*IR.3*OD.zh*MS.-1*RMS.-1*TRA.false*LD.1026083; TAUD=LA-1544354601720-1*RDD-1-2018_12_09*HDD-884472-2018_12_23.2018_12_24.1*LD-932203-2018.12.23.2018.12.24*LG-932205-2.1.F.'
}


def get_attractions(url,data=None):
    wb_data = requests.get(url)
    time.sleep(2)#每隔2秒获取一次，防反爬
    soup = BeautifulSoup(wb_data.text, 'lxml')
    titles = soup.select('.listing_title')
    imgs = soup.select('.photo_image')
    cates=soup.select('.wrap')
    for title, img, cate in zip(titles, imgs, cates):
        data = {
            'title': list(title.stripped_strings)[0],
            'img': img.get('src'),
            'cate': list(cate.stripped_strings)
        }
        print(data)

def get_favs(url,data=None):
      #url_saves='https://www.tripadvisor.cn/Tourism-g293920-Phuket-Vacations.html'
      wb_data=requests.get(url,headers=headers)
      soup=BeautifulSoup(wb_data.text,'lxml')
      titles=soup.select(' a.hotel.name')
      imgs=soup.select('img.photo_image')
##<a href="/Attraction_Review-g1215780-d1161264-Reviews-Kata_Noi_Beach-Karon_Phuket.html" onclick=" event.stopPropagation();ta.setEvtCookie('Attraction_List_Click', 'POI_click', 'name', 1, '/Attraction_Review')" target="_blank">卡特诺</a>HTL_FAVS > li:nth-child(2) > a.photo.posRel > div > div:nth-child(3)
      metas=soup.select('.rank')
      for title,img,meta in zip(titles,imgs,metas):
            data={
                  'title':title.get_text(),
                  'img':img.get('src'),
                  'meta':list(meta.stripped_strings)
                }
            print(data)
for singe_url in urls:
    get_attractions(singe_url)