#函数定义
# def Xu():
#     print("bobo")
# Xu()


# def circle_area(r):
#     return 3.14 * (r ** 2)
# print(circle_area(10))
#
# def rectangle_area(l,w):
#     """
#
#     :param l:
#     :param w:
#     :return:长方形的面积
#     """
#     return l*w
# print(rectangle_area(5,6))
#
#
# def circle_area_length(r):
#     """
#     根据圆的半径，计算圆的面积和周长
#     :param r: 圆的半径
#     :return: 圆的面积，圆的周长
#     """
#     return 3.14 * r ** 2,round(2*3.14*r,1)
# a,b = circle_area_length(5)
# print(a)
# print(b)
# help(circle_area_length) #help:print 出函数的说明文档


def function_a():
    print(1)
    function_b()
    print(5)
def function_b():
    print(2)
    function_c()
    print(4)
def function_c():
    print(3)
function_a()
print("函数调用完毕")

