# import random
# num = random.randint(1,100)
# while True:
#     m = int(input("请输入数字："))
#     if m == num:
#         print("答对了")
#         break
#     elif m > num:
#         print("大了")
#     else:
#         print("小了")

# m = 0
# for i in range(0,1001,5):
#     m = m + i
# print("1~1000内所有5的倍数之和为：",m)


m = "auisaiusuyewewgbcwicoixiozmqnnansanabwbxyaxaa"
n = 0
q = 0
for i in m:
    if i == "a":
        n += 1
    elif i == "i":
        q += 1
print(f"该字符串中\'a\'的数量为{n}个，\'i\'的数量为{q}个")

