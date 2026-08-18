# dict1 = {"王琳":670,"李牧完":688,"林鸿":667,"都江堰":675,"少昊军":647}
# for k in dict1.keys():
#     m = dict1[k]
#     print(f"{k}:{m}")
#     print(f"{k}:dict1[{k}]")
# print(dict1)
# dict1["许杨波"]=700
# print(dict1)
# dict1["许杨波"]=701
# print(dict1)
# print(dict1["许杨波"])
# print(dict1.get("许杨波"))
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())
# m = dict1.pop("许杨波")
# print(m)
# del dict1["王琳"]
# print(dict1)


#设计购物车系统：
#1.制作菜单：
print("欢迎使用购物车系统！")
menu ="""
##########  购物车系统  ##########
#          1.添加购物车          #
#          2.修改购物车          #
#          3.删除购物车          #
#          4.查询购物车          #
#          5.退出购物车          #
#          6.查看购物车          #
#################################
"""
shopping_cart = {}
while True:
    print(menu)
    choice = input("请输入要执行的操作（1~6）：")
    match choice:
        case "1":
            goods_name = input("请输入商品名称：")
            goods_price = input("请输入商品价格：")
            goods_num = input("请输入商品数量：")
            if goods_name in shopping_cart:
                print("已有重复商品")
            else:
                shopping_cart[goods_name] ={ "price":goods_price, "num":goods_num}
                print(shopping_cart)
        case "2":
            goods_name = input("请输入要修改的商品名称：")
            if goods_name not in shopping_cart:
                print("该商品还未添加到购物车中，请先添加")
            else:
                goods_price = input("请输入商品的最新价格：")
                goods_num = input("请输入商品的数量：")
                shopping_cart[goods_name] = { "price":goods_price, "num":goods_num}
                print("已修改成功")
        case "3":
            no = input("请输入要删除的商品名称：")
            if no in shopping_cart:
                del shopping_cart[no]
                print("已删除")
            else:
                print("该商品不存在，请确认后输入")
        case "4":
            yes = input("请输入要查询的商品名称：")
            if yes in shopping_cart:
                mmm = shopping_cart[yes]
                print("名称：", yes, "价格为：",mmm["price"],"数量为：",mmm["num"])
            else:
                print("该商品不存在，请核对后输入！")
        case "5":
            print("bye~")
            break
        case "6":
            print(shopping_cart)
        case _:
            print("请重新输入1~5内数字！")









