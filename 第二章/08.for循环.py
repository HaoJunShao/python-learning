# msg = input("请输入要遍历地字符串：")
# for m in msg:
#     print(f"元素:{m}")
# else:
#     print("遍历结束")


#计算100~500之间所有3的倍数的和：
# total = 0
# for i in range(102,500,3):
#     print(i)
#     total += i
# else:
#     print("结果为：",total)

#嵌套循环：打出一个长度为5，宽度为10的长方形：

# 打印九九乘法表：
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}*{i}={i*j}",end="  ")
#     print()

# m = int(input("请输入直角三角形的直角边长度："))
# for i in range(1,m+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
n = 0
m = int(input("请输入行数："))
for i in range(1,m+1):
    if i % 2 == 1:
        while n <= m:
            print("#",end="")
            n += 1
    print()



