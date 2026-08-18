# print("Hello")
# print(type(1))
# print(type(1.2))
# print(type(True))
# print(type(None))
from glob import magic_check
from pickletools import string1

# num = 3.0
# print(isinstance(num,float))
# print(isinstance(num,int))
# print(isinstance(num,str))
# print(isinstance(num,bool))
# s1 = ("Hello")
# s2 = 'Python'
# s3 = """
# Hello:
#     欢迎来到天津
#     祝你大学学习生活愉快！
# """
# print(s1,s2,s3)
# #转义字符：\'  \"  \n  \t
# msg = 'It\'s very good'
# msg2 = "hello 的意思是\"你好\""
# print(msg2)
# print('欢迎来到天津\n\t祝你大学学习生活愉快！' )


#字符串的拼接
# s1 = "人生苦短"   ",我用Python"     "\n\tAre you OK?"
# print(s1)
#
# msg1 = '人生苦短'
# msg2 = "我用Python"
# print("龟叔说:"+msg1+","+msg2)
# name = "Shaohaojun"
# age = 18
# pro = "软件工程"
# hobby = "唱、跳、rap、篮球"
# print("Hello!，大家好：\n\t我的名字是"+name+",今年"+str(age)+"岁,专业是"+pro+",我的爱好是"+hobby+"\n\tmusic")

# 字符串的格式化
# name = "Shaohaojun"
# age = 18
# pro = "软件工程"
# hobby = "唱、跳、rap、篮球"
# print("Hello!，大家好：\n\t我的名字是 %s ,今年 %s 岁,专业是 %s ,我的爱好是 %s \n\tmusic"%(name,age,pro,hobby))

# 方式二
name = "Shaohaojun"
age = 18
pro = "软件工程"
hobby = "唱、跳、rap、篮球"
print(f"Hello!，大家好：\n\t我的名字是 {name} ,今年 {age} 岁,专业是 {pro} ,我的爱好是 {hobby} \n\tmusic")



