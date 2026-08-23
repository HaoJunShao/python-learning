# def add(x,y):
#     return x+y
# def subtract(x,y):
#     return x-y
# def multiply(x,y):
#     return x*y
# def divide(x,y):
#     return x/y
# def calc(x,y,oper):
#     return oper(x,y)
# print(calc(114,514,subtract))


# out_line = lambda : print("-----------")
# out_line()
# add = lambda a,b: a+b
# print(add(1,2))

# data_list = ["python","C","C++","Java","Go"]
# data_list.sort(key = len)
# print(data_list)
#
# data_list = ["python","C","C++","Java","Go"]
# data_list.sort(key = lambda x:len(x))
# print(data_list)


#计算n的阶乘：
# def func(m):
#     s = 1
#     for i in range(1,m+1):
#         s = s * i
#     print(s)
# func(5)

# def func(m):
#     if m==1:
#         return 1
#     else:
#         return m * func(m - 1)
# n = func(5)
# print(n)


"""
案例2
"""

def calc_order_price(*args: tuple[str,int,int],coupon = 0.0,score = 0.0,express = 0.0)->float:
    total_list = [i[1] * i[2] for i in args]
    total_price = sum(total_list)
    if total_price >= 5000 and coupon <= total_price:
        total_price = total_price - coupon
    if total_price >= 5000 and score // 100 <= total_price:
        total_price = total_price - score // 100
    total_price = total_price + express
    return total_price
m = calc_order_price(("手机",9999,2),("耳机",999,1),("平板",4999,3),coupon = 100,score = 3000,express = 9.9)
print(m)


#开发代码要点：
#1.既然是一批商品，意味着数量未知，在设置形参是应使用不定未知变量
#2.不定位置变量本身的元素可以为一个个单独的小的元组或者列表，这样设置则可以满足题目中对于商品的描述
#3.元组、列表和字符串都可以使用索引功能，即意味着具有顺序
#4.对args进行类型注释，可以自动封装进元组中，只需要对每一个单独的元素进行注解即可




