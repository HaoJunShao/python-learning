#1.导入模块：
# from utils import my_fun
# my_fun.log_seperator1()
#注意：如果要通过 from utils import * 导入包下的所有模块，需要__init__.py文件中添加__all__ = []
# from utils import *
# my_fun.log_seperator1()
# print(my_var.PI)
#2.导入模块中具体功能：
from utils.my_fun import *
log_seperator1()
