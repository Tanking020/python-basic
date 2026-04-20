#打印一个宽为a长为b的长方形
"""
try:
    a = int(input("请输入长方形的宽："))
    b = int(input("请输入长方形的长："))
except ValueError:
    print("请输入整数！！！")
    exit()

for i in range(a):
    for j in range(b):
        print("*",end="")
    print()
"""

#打印99乘法表
"""
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j}",end=" ")
    print()
"""

#流程控制语句
"""
count = input("请输入账号：")
key = input("请输入密码：")
while count == "" or key == "":
    print("账号或密码不能为空！")
    count = input("请输入账号：")
    key = input("请输入密码：")

while not ((count == "admin" and key == "666888") or
           (count == "zhangsan" and key == "123456") or
           (count == "taoge" and key == "888666")):
    print("用户名或密码错误，请重新输入！！！")
    count = input("请输入账号：")
    key = input("请输入密码：")
print("登录成功，进入B站首页~")
exit()
#这样写明显有个问题就是密码错误后又要重新判断是不是为空，所以这么写不好
"""

#改用while True循环语句（！！！）：
"""
while True:  #只要不break结束就会一直循环
    name = input("请输入账号：")
    key = input("请输入密码：")

    if name == "" or key == "":
        print("账号或密码不能为空！！！")
        continue
        #这里continue跳过此次循环重新输入，就可以避免浪费时间读下面其他代码了

    valid = ((name == "admin" and key == "666888") or
             (name == "zhangsan" and key == "123456") or
             (name == "taoge" and key == "888666"))

    if not valid:
        print("账号或密码错误，请重新输入！！！")
        continue
    else:
        print("登录成功，进入B站首页~")
        break
"""#这样就很好了^_^
#注意：continue和break都只会应用至所在的最内层循环（近视眼）

#巩固流程控制语句：
#猜大小游戏
"""
import random
random_number = int(random.randint(1, 100))

while True:


    try:
        user_num = int(input("请输入数字:"))
    except ValueError:
        print("您输入的格式有误！！！")
        continue
    if user_num > random_number:
        print("您输入的数字比实际数字更大")
        continue
    elif user_num < random_number:
        print("您输入的数字比实际数字更小")
        continue
    else:
        print("您输入的数字就是实际数字！！！")
        break
    #一定注意不要将随机数生成语句写到循环内部！！！
"""

"""
#几种列表操作
s = [1,22,7,33,4,4,5]
#切片
s1 = s[1:5:2]
print(s1)

#以下操作直接改变列表但不返回值！所以s2 = s.append(7)返回的是None!!!

#末端增加
s.append(7)
print(s)

#列表反序
s.reverse()
print(s)

#列表排序
s.sort()#从小到大
print(s)

s.sort(reverse=True)#从大到小
print(s)

b = ["111","22","1","aaa"]
b.sort(key=len)#按照长度从短到长排序
print(b)

b.sort(key=len, reverse=True)
print(b)#按照长度从长到短排序

#往指定索引之前插入元素
s.insert(2,90)
print(s)

#删除列表中元素（与del区分，del删除但不返回，pop删除后返回）(pop()默认删除最后一个)
s.pop(2)
print(s)

#移除从左往右第一个等于目标值的元素(要从右往左删除只能先反转列表)
s.remove(7)
print(s)
"""

"""
#将用户输入的10个数字进行从大到小排序，并且输出最大值，最小值，平均值：
s = []

for i in range(10):
    s.append(int(input(f"请输入数字{i+1}:")))#易错点：s = []是空列表不能直接执行s[i] = 的赋值操作

s.sort(reverse=True)
print(s)

max = s[0]
min = s[-1]
ave = sum(s) / len(s)
print(f"您输入的10个数字的最大值为{max},最小值为{min},平均值为{ave}")
"""

#合并两个列表中的元素，并对合并的结果进行去重处理
"""
num_list1 = [19,23,54,64,875,20,109,232,123,54]
num_list2 = [55,80,72,35,60,123,54,29,91]

#我的思路：先合并（遍历的方式添加(append)），再排序，再遍历删去重复元素

#利用循环的合并思路

for num0 in num_list2:#对列表中元素进行的遍历
    num_list1.append(num0)#切记修改的过程返回的都是None而不是值，修改过程不能直接被赋值给变量！！！
num = num_list1

#另一种合并思路：利用解包进行列表合并

num = [*num_list1,*num_list2]#利用*进行解包（相对应地有组包地概念）


#第三种合并思路：(列表的+合并)（最简洁）
num = num_list1 + num_list2

num.sort()
#删去重复元素（经典操作）：需要创建一个空列表执行经典操作！！！
num_new = []

for num0 in num:
    if num0 not in num_new:
    #判断元素是否在列表中并返回布尔值（利用in）
        num_new.append(num0)

print(num_new)
"""