#绘制五角星
import turtle

def draw_recursive_pentagram(size): #迭代方式绘制五角星
    count=1
    while count<=5:
        turtle.forward(size)
        turtle.right(144)
        count+=1
    if size<=160:
     draw_recursive_pentagram(size+20)

"""使用函和实现
def pentagram(size):
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1
"""

def main():

 #控制画笔，初始值从画布中心位置开始
    turtle.penup()  #抬起笔
    turtle.backward(200) #反向（向左）移动200
    turtle.pendown()    #放下笔
    turtle.pensize(3)   #笔尺寸
    turtle.pencolor('orange') #画笔颜色

    size=50
    draw_recursive_pentagram(size)#调用递归函数

    """"调用函数
    while size<=160:
        pentagram(size)
        size=size+20
    """
    turtle.exitonclick()


if __name__=='__main__':
    main()