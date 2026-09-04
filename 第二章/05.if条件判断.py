# score = int(input("请输入你的高考分数："))
# if score >= 680:
#     print("欢迎光临全家")
# if score <= 680:
#     print("四年后再见吧")
#     print("不管怎样，祝你拥有一段快乐美好的大学生活！")
# print("------------------")


# ok_account = "1"
# ok_password = "2"
# account = input("请输入
# 您的账号：")
# password = input("请输入您的密码：")
# if account == ok_account and password == ok_password:
#     print("登陆成功")
# else:
#     print("登陆失败！")


# num = int(input("请输入年份："))
# if (num % 100 == 0 and num % 400 != 0) or (num % 4 != 0):
#     print(f"{num}年是平年")
# else:
#     print(f"{num}年是闰年")


# 练习题：
# num = int(input("请输入文本："))
# if num == 0:
#     print("False,请重新输入")
# else:
#     if num % 2 == 0:
#         print("偶数")
#     else:
#         print("奇数")


# num = int(input("请输入文本："))
# if num == 0:
#     print("既不是正数，也不是负数")
# else:
#     if num > 0:
#         print("正数")
#     else:
#         print("负数")
# if num == 0:
#     print("是0")
# elif num > 0:
#     print("正数")
# else:
#     print("负数")



# ID1 = 1
# ID2 = 2
# ID3 = 3
# pw1 = 000
# pw2 = 111
# pw3 = 222
# num1 = int(input("请输入账号"))
# num2 = int(input("请输入密码"))
# if (num1 == ID1 and num2 == pw1) or (num1 == ID2 and num2 == pw2) or (num1 == ID3 and num2 == pw3):
#     print("登陆成功")
# else:
#     print("登陆失败")


"""
num = int(input("请输入购物金额："))
if num >= 500:
    print("应该支付",num*0.8,"元")
elif 300 <= num < 500:
    print("应该支付", num * 0.9, "元")
elif 100 <= num < 300:
    print("应该支付", num * 0.95, "元")
else:
    print("无优惠，应支付",num,"元")
"""
a = int(input("请输入三角形的边长："))
b = int(input("请输入三角形的边长："))
c = int(input("请输入三角形的边长:"))
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("是等边三角形")
    elif a==b or b==c or c==a:
        print("是等腰三角形")
    else:
        print("是普通三角形")
else:
    print("不能构成三角形")





