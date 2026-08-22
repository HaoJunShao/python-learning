#全局变量与局部变量：
# num = 1
# def func():
#     num = 2
#     print(num)
# func()
# print(num)

# num = 1
# def func():
#     global num
#     num = 100
#     print(num)
# func()
# print(num)

# def func(a,b,c,d):
#     print(f"姓名:{a} 年龄:{b} 性别：{c} 籍贯：{d}")
#     return "姓名：",a,"年龄：",b,"性别：",c,"籍贯：",d
# m = func("张三","20","男","北京")
# n = func(b = "28",a = "李四",d = "福建",c = "女")
# n1 = func("李四",20,d = "日本",c = "未知")

# def func(a,b,c = "男",d = "美国"):
#     print(f"姓名:{a} 年龄:{b} 性别：{c} 籍贯：{d}")
#     return "姓名：",a,"年龄：",b,"性别：",c,"籍贯：",d
# m = func("张三","20")
# n = func(b = "28",a = "李四",d = "福建",c = "女")


#不定长参数：
# def cal_data(*args):
#     print(max(args))
#     print(min(args))
#     print(round(sum(args)/len(args),4))
# cal_data(1.13,3543534,5435,7878,43673,77547547)
#
# def cal_data(*a):
#     print(max(a))
#     print(min(a))
# cal_data(1.13,3543534,5435,7878)

def cal_data(*args,**kwargs):
    """

    :param args: 不定长位置参数
    :param kwargs:不定长关键字参数
    :return:
    """
    a = max(args)
    b = min(args)
    c = sum(args)/len(args)
    if kwargs.get("round") is not None:
        c = round(c,kwargs.get("round"))
    if kwargs.get("print"):
        print(f"最大值为：{a}，最小值为：{b}，平均值为：{c}")

cal_data(1.13,3543534,5435,7878)
cal_data(1.13,3543534,5435,7878,print=True,round=2)
cal_data(1.13,3543534,5435,7878,print=False,round=2)


# def cal_data(*a):
#     print(max(a))
#     print(min(a))
# cal_data(1.13,3543534,5435,7878)



