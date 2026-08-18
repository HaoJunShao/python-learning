# s = 'Hello-Python'
# print(s[-8])
# for i in s:
#     print(i)
#     print(s[::-1])


s = 'oHello-Python-Hello-Worldo'
a = s.find("Python")
print(a)
b = s.count("-")
print(b)
c = s.upper()
print(c)
d = s.lower()
print(d)
e = s.split("-")
print(e)
f = s.strip("o")
print(f)
g = s.replace("-","~")
print(g)
print(s.startswith("o"))
print(s.endswith("m"))


#验证用户邮箱格式是否满足需求：
# m = input("请输入您的邮箱：")
# if m.count(".") == 0 or m.count("@") == 0:
#     print("邮箱格式错误")
# else:
#     print("邮箱格式正确")

# m = "amsjxnfnwfajnjdnuqi"
# print('i' in m)



# m = "上海自来水来自海上"
# if m ==  m[::-1]:
#     print("是回文序列")
# else:
#     print("不是")


# n = input("请输入文本：")
# m = n[::-1]
# q = m.upper()
# print(q)
# for i in q:
#     print(i)



