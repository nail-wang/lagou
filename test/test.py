#1.定义有参数，有返回值的情况
def have(parameter):
    print(f"这个函数有参数{parameter}")
    return "这个函数有返回值"

#2.定义有参数，无返回值的情况，无返回值的默认返回值为None
def have_no_return(parameter):
    print(f"这个函数有参数{parameter}，无返回值")

#3.定义无参数，有返回值的情况
def no_parameter():
    print(f"这个函数无参数")
    return "这个函数有返回值"

#4.定义无参数，无返回值的情况，无返回值的默认返回值为None
def no_no():
    print(f"这个函数无参数，无返回值")