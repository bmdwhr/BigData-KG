
import pandas as pd


def main():
    """
        主函数
    """
    aqi_data = pd.read_csv('china_city_aqi.csv')
    print('基本信息：')
    print(aqi_data.info())

    print('数据预览：')
    print(aqi_data.head())

    # 基本统计
    print('AQI最大值:', aqi_data['AQI'].max())
    print('AQI最小值：', aqi_data['AQI'].min())
    print('AQI均值：', aqi_data['AQI'].mean())#平均值

    # top10
    top10_cities = aqi_data.sort_values(by=['AQI']).head(10)#排序，空气最好的城市，默认升序，按'AQI'升序
    print('空气质量最好的10个城市：')
    print(top10_cities)

    # bottom10
    # bottom10_cities = aqi_data.sort_values(by=['AQI']).tail(10)#最后10条
    bottom10_cities = aqi_data.sort_values(by=['AQI'], ascending=False).head(10)
    print('空气质量最差的10个城市：')
    print(bottom10_cities)

    # 保存csv文件
    top10_cities.to_csv('top10_aqi.csv', index=False)#pd.to_csv写入csv文件
    bottom10_cities.to_csv('bottom10_aqi.csv', index=False)
    


if __name__ == '__main__':
    main()
