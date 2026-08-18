# day = input("请输入日期：")
# match day:
#     case "1"|"2"|"3"|"4"|"5":
#         print("工作日")
#     case "6"|"7":
#         print("休息日")
#     case _:
#         print("错误")


y = input("请输入你想要运算的运算符：")
a = int(input("请输入你的第一个数字："))
b = int(input("请输入你的第二个数字："))
match y:
    case "+":
        print("结果是",a+b)
    case "-":
        print("结果是：",a-b)
    case "*" :
        print("结果是：",a*b)
    case "/" if b != 0:
        print("结果是：",a/b)
    case _:
        print("无")



#游戏角色动作开发：
# a = input("请输入要执行的操作：")
# match a:
#     case "上"|"w"|"W":
#         print("跳")
#     case "下"|"s"|"S":
#         print("蹲")
#     case "左"|"a"|"A":
#         print("左")
#     case "右"|"d"|"D":
#         print("右")