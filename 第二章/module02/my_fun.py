#常量(不会发生变化的数据；常量的名称全大写)
PI = 3.1415926
def log_seperator1():
    print("- " * 30)#"- "重复输出30次，不用再手打了！
print(__name__)
if __name__ == "__main__":
    log_seperator1()

__all__ = ['PI']
