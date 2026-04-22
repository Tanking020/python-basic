#生成1-20的平方列表
#方法1：传统循环插入
"""
num_list = []
for i in range(1,21):
    num_list.append(i**2)
print(num_list)
"""

#方法2：利用列表推导式语法 列表 = [要插入的值 for i in 序列/列表]
"""
num_list = [i**2 for i in range(1,21)]
print(num_list)
"""

#从原始列表中提取所有偶数，并计算其平方，组成一个新的列表
"""
num_list = [19,23,54,64,87,20,109,232,123,43,26,55,72]

num_list2 = [i**2 for i in num_list if i % 2 == 0]#新表 = [要插入的值 for i in 序列/列表 if 条件]
print(num_list2)
"""

#将如下列表中的正数提取出来并封装为一个新的列表
"""
list1 = [11,2,31,4,-5,15,17,28,49,10,-11,16,54,-14,36,-16,87,-39]

list2 = []
for i in list1:
    if i > 0:
        list2.append(i)

print(list2)
"""
#法2（列表推导式语法）
"""
list1 = [11,2,31,4,-5,15,17,28,49,10,-11,16,54,-14,36,-16,87,-39]

list2 = [i for i in list1 if i >0]
print(list2)
"""

#字符串常用操作：
#！！！注意：列表是可变的，修改列表并不会返回值，字符串是不可变的，字符串操作不是修改而是返回新的字符串！！！
"""
str = "python"
#查找子串
f = str.find("th")
print(f)

#统计子串出现次数
c = str.count("th")
print(c)

#将字符串中所有字母转换为大写
u = str.upper()
print(u)

#将字符串中所有字母转换为小写
l = str.lower()
print(l)

#将字符串按指定的分隔符分割为列表
s1 = str.split("o")
print(s1)

s2 =str.split("t")
print(s2)

#去除字符串两端的空白字符或者指定字符
st = str.strip("p")
print(st)

#将字符串中的指定子串替换为新的子串
r = str.replace("p","o")
print(r)

#检查字符串是否以指定子串开头，返回布尔值
sta =str.startswith("py")
print(sta)

print(str)
"""

#邮箱格式验证
"""
met = input("请输入邮箱：")
f1 = met.count("@")
print(f1)
if f1 == 1 and "." in met:#用in运算符检测子串是否存在于指定字符串中（返回布尔值）
    print("邮箱格式输入正确")
else:
    print("邮箱格式输入错误")
"""

#元组tuple：仅有两种查询操作：
#index:查询某个元素在元组中从左往右第一次出现的位置
#count:查询某个元素在元组中出现的次数

#注意！定义单元素元组时候不能用（100），必须用（100，）没这个逗号就变成int类型了
"""
tuple1 = (2,3,4,5,6)
a,*b,c = tuple1
print(type(a))
"""

#元组的组包与解包
#现有三个变量，分别为：a=100,b=200,c=300,现需要将这三个变量值进行交换，将a,b,c的值分别赋值给c,a,b，并且将其输出到控制台
"""
a,b,c=100,200,300

#tuple1 = a,b,c#组包
#print(tuple1)
#c,a,b = tuple1#解包

#合并：
c,a,b = a,b,c
print(a,b,c)
"""

"""
根据学生成绩单完成如下需求：
1、计算每个学生总分、各科平均分，然后一并输出出来
2、统计各科成绩的最高/最低分并且输出
3、查找平均分大于90的学生并输出
"""
#数据不能修改，所以这里用元组进行存储
"""
students = (("S001","王林",85,92,78),
            ("S002","李木碗",92,88,95),
            ("S003","十三",78,85,82),
            ("S004","曾牛",88,79,91),
            ("S005","周铁",95,96,89),
            ("S006","王卓",76,82,77),
            ("S007","红蝶",89,91,94),
            ("S008","徐利果",75,69,82),
            ("S009","许木",86,89,98),
            ("S010","遁天",66,59,72),)
print(students)

#第一步
print("学号 \t 姓名 \t 语文 \t 数学\t 英语\t 总分\t 平均分")#\t为制表符，主要作用是方便对齐
#方式1
# for stu in students:
#     total = stu[2] + stu[3] + stu[4]
#     avg = total / 3
#     print(f"{stu[0]} \t {stu[1]} \t {stu[2]} \t {stu[3]} \t {stu[4]} \t {total} \t {avg:.1f}")#保留一位小数并且按浮点数存储

#方式2：元组的解包操作(有效提升可读性)
for id,name,chinese,math,english in students:
    total = chinese + math +english
    avg = total / 3
    print(f"{id} \t {name} \t {chinese} \t {math} \t {english} \t {total} \t {avg:.1f}")#保留一位小数并且按浮点数存储

#第二步（使用列表方便插入和排序，如果需要的话用完再转元组）
chi_sco = [s[2] for s in students]
mat_sco = [s[3] for s in students]
eng_sco = [s[4] for s in students]

min_chi = min(chi_sco)
max_chi = max(chi_sco)
min_mat = min(mat_sco)
max_mat = max(mat_sco)
min_eng = min(eng_sco)
max_eng = max(eng_sco)

print()
print(f"语文：最高{max_chi},最低{min_chi}；数学：最高{max_mat},最低{min_mat}；英语：最高{max_eng},最低{min_eng}")
print()

#第三步
for stu in students:
    total = stu[2] + stu[3] + stu[4]
    avg = total / 3
    if avg > 90:
        print(f"{stu[1]}是优秀学生")
"""