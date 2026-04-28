# 函数定义括号内为形参，调用时传入的参数是实参
# 定义时候要注意返回
# 要先定义后调用(特殊情形：定义函数时候可调用未定义的函数并在之后补充定义)

#函数嵌套调用：栈的逻辑-先入后出
"""
def function_a():
    print("a-before")
    function_b()
    print("a-after")

def function_b():
    print("b-before")
    function_c()
    print("b-after")

def function_c():
    print("c")

function_a()
"""

#案例：
# def function_score(S):
#     """
#     此函数用于根据传入的分数判别其等级
#     :param S: 分数
#     :return: 等级
#     """
#     if 100 >= S >= 90:
#         level = "A"
#     elif 90 > S >= 75:
#         level = "B"
#     elif 75 > S >= 60:
#         level = "C"
#     elif 0 <= S < 60:
#         level = "D"
#     else:
#         print("输入有误！")
#     return level
#
# print()
# fc = function_score(70)
# print(fc)

# ！！！全局变量：在函数内外都可用，局部变量：仅仅在函数内部可用，函数调用结束后自动销毁（在函数外部无法访问函数内部的局部变量）！！！
# 在函数中定义全局变量需要使用关键字：global,否则默认定义为局部变量，函数外部声明的变量为全局变量
"""
num = 1
def test():
    num1 = 1
    global num2 # 只能声明变量！不能“同时”赋值！！！
    num2 = num + 1
    num3 = num
    return num3 # return返回的是值
test()
print(num2)
print(num1) # num1是局部变量，函数调用后被销毁了
"""

# 传参方式：1、位置参数（按序传入）xx ；2、关键字参数（按键值对传入）xx = yy
# 如果位置参数与关键字参数混用，必须先传完所有位置参数后写关键字参数，关键字参数之间无位置要求

# 传入新参数会改变默认参数

# 长度不确定时候可用*实现基于位置传递的不定长参数——元组
# 更准确地说，*args（先写） - 基于位置传递的不定长参数（主要处理数据） 把零散的位置参数打包成元组，**kwargs（后写） - 基于关键字的不定长参数（主要处理选项） 把关键字参数打包成字典

# 函数的特殊类型参数：函数
"""
def multiply(a,b):
    return a * b

def oper(a,b,oper):
    return oper(a,b)

print(oper(4,5,multiply))
"""

# 匿名函数（通常作为高阶函数的参数使用）：lambda = 参数 ：函数体（表达式） 不允许换行，不需要return返回，表达式结果就是返回值
# 对匿名函数用赋值方式命名即可调用

"""
def add(x,y):
    return x + y

add2 = lambda x,y: x + y

print(add(3,4))
print(add2(1,2))
"""

# 递归函数(在函数中自己调用自己)的应用 可以用栈的思维理解，类似函数嵌套,在这个过程中函数会被多次调用
# 经典：n的阶乘的递推公式：f(n) = n * f(n-1) !!!
"""
def factorial(n):
    if n == 0: # 不要忘记增加递归结束条件
        return 1
    else:
        return n * factorial(n-1) # 在函数体中调用函数自身，称为递归函数

print(factorial(6))
"""
# 任何递归都能改写为while循环，反之亦然
# 先层层递进，再逐层回归，所以称为递归 全部依次入栈 - 达到终结点 - 全部依次出栈

# 案例：商品信息处理(\\为整数除法，向下取整)
# def goods_test(*args,coupon = 0 , score = 0 , express = 0.0):
#     """
#     此函数用于计算商品价格
#     :param args: 商品名称，价格，数量
#     :param coupon: 优惠券
#     :param score: 积分
#     :param express: 运费
#     :return:商品最终价
#     """
#     # 1、计算商品总金额：
#     total_price = [goods[1] * goods[2] for goods in args]
#     total_cost = sum(total_price)
#
#     # 2、扣减优惠券
#     if total_cost >= 5000 and coupon <= total_cost:
#         total_cost -= coupon
#
#     # 3、执行积分抵扣
#     if total_cost >= 5000 and score // 100 <= total_cost:
#         total_cost -= score // 100
#
#     # 4、添加运费
#     total_cost += express
#
#     return total_cost

# # 测试 (不定长参数放前面，后面要用关键字参数方式传入，也可将不定长参数放最后，前面仍然用位置参数)
# # 在前面定义运费为0（int型）也可以，传入float型会出黄色波浪线但不会影响运行
# GOODS = goods_test(("电脑",6000,1),("手机",2000,1),("衣物",200,4),coupon = 2000,score = 100,express = 73.5)
# print(GOODS)

# 类型注解(提升代码可维护性，加不加不影响运行) 语法 - a: int = 695 ; names: list[str] = ["A","C","E"]
# options2: dict[str,int] = {"count":2,"total":10} 用这种类型注释方式定义，写的时候就能提示问题（但是不会影响运行）
# 可以用 | 表示或，允许整数类型或者浮点数类型等

# 类型推断（同样只提示，不影响传参、程序运行！！！）：python解释器自动推出数据类型，在对变量进行直接赋值，或者涉及到变量运算、容器推导等场景时候，解释器会自动推导出变量的类型

# 函数类型注解：主要为函数的参数和返回值添加类型注解
# def s(scores:list[int])
# 语法结构：def 函数名(参数: 类型) -> 返回值类型:
#             return 值
# def test(args:tuple[str,float,int],coupon = 0) -> tuple[int,int,float]:
