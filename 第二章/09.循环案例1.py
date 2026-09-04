# while True:
#     m = input("请输入用户名：")
#     n = input("请输入密码：")
#     if m == "" or n == "":
#         print("用户名或密码为空，请重新输入！")
#         continue
#     elif (m == "123" and n == "abc") or (m == "456" and n == "def"):
#         print("登陆成功")
#         break
#     else:
#         print("登陆失败，请重新输入！")


# i = 0
# while i<=4:
#     m = input("请输入用户名：")
#     n = input("请输入密码：")
#     if m == "" or n == "":
#         print("用户名或密码为空，请重新输入！")
#         i = i + 1
#         continue
#     elif (m == "123" and n == "abc") or (m == "456" and n == "def"):
#         print("登陆成功")
#         break
#     else:
#         print("登陆失败，请重新输入！")
#         i += 1
# else:
#     print("免费次数已用完，你没机会了")


#打印国际象棋：
for i in range(1,5):
    for j in range(1,10):
        if (i + j) % 2 == 0:
            print("黑",end="")
        else:
            print("白",end="")
    print()
