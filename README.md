# python-basic
basic-grammar
# Python 基础练习：循环与条件判断

**学习日期**：2026.04.19

---

## 📚 今日学习内容

| 知识点 | 练习题目 | 状态 |
|:---|:---|:---:|
| `while` 循环 | 1到100所有偶数和 | ✅ |
| `for` 循环 | 100到500所有3的倍数和 | ✅ |
| `range()` 函数 | 理解左闭右开区间 | ✅ |
| 条件判断 | 三角形类型判断 | ✅ |
| 异常处理 | 简单计算器 | ✅ |
| 列表操作 | 三角形边长输入 | ✅ |

---

## 💻 代码示例

### 1. 1到100偶数和（while循环）

```python
i = 1
total = 0
while i <= 100:
    if i % 2 == 0:
        total += i
    i += 1
print(f"1到100之间的所有偶数之和为{total}")  # 2550
```

### 2. 100到500所有3的倍数和（for循环）

```python
total = 0
for i in range(100, 501):
    if i % 3 == 0:
        total += i
print(f"100到500之间所有3的倍数的数字之和为：{total}")  # 39900
```

### 3. 三角形判断

```python
sides = []
for i in range(1, 4):
    side = float(input(f"请输入边长{i}："))
    sides.append(side)

a, b, c = sorted(sides)

if a + b <= c:
    print("这不是一个三角形")
elif a == b == c:
    print("等边三角形")
elif a == b or b == c:
    if a**2 + b**2 == c**2:
        print("等腰直角三角形")
    else:
        print("等腰三角形")
elif a**2 + b**2 == c**2:
    print("直角三角形")
else:
    print("普通三角形")
```

### 4. 简单计算器

```python
try:
    num1 = float(input("请输入数字1:"))
    op = input("请输入运算符:")
    num2 = float(input("请输入数字2:"))
except ValueError:
    print("输入有误！")
    exit()

match op:
    case "+": result = num1 + num2
    case "-": result = num1 - num2
    case "*": result = num1 * num2
    case "/":
        if num2 == 0:
            print("除数不能为0！")
            exit()
        result = num1 / num2
    case _:
        print("运算符有误！")
        exit()

print(f"{num1} {op} {num2} = {result}")
```

---

## 🧠 关键知识点总结

### `range(a, b)` 的区间
- **左闭右开**：包含 `a`，不包含 `b`
- 示例：`range(2, 6)` → `2, 3, 4, 5`

### `exit()` vs `break`
| 方法 | 作用 |
|:---|:---|
| `exit()` | 结束整个程序 |
| `break` | 只退出当前循环 |
| `return` | 只退出当前函数 |

### 列表 `append()`
- 向列表末尾添加元素
- `sides.append(side)` 将 `side` 加入 `sides` 列表

### 解包赋值
```python
a, b, c = sides  # 列表元素分别赋给 a, b, c
```

---

## 📁 文件结构

```
Python-Basics-Learning/
├── README.md
├── 01_even_sum.py          # 1-100偶数和
├── 02_multiples_sum.py     # 100-500的3倍数和
├── 03_triangle.py          # 三角形判断
├── 04_calculator.py        # 简单计算器
└── 05_loop_examples.py     # 循环综合练习
```

---

## 🔄 后续计划

- [ ] 函数封装练习
- [ ] 文件读写操作
- [ ] 小游戏开发（猜数字、剪刀石头布）
- [ ] 继续数值分析算法实现

---

## 📖 参考资料

- [Python 官方文档](https://docs.python.org/3/)
- [廖雪峰 Python 教程](https://www.liaoxuefeng.com/wiki/1016959663602400)

---

*持续更新中...*
```

---

## 二、如果你想要更简洁的版本

```markdown
# Python 基础练习 (2026.04.19)

## 练习列表

1. **1-100偶数和** → `01_even_sum.py`
   - while循环 + 取模判断
   - 结果：2550

2. **100-500的3倍数和** → `02_multiples_sum.py`
   - for循环 + range() + 取模判断
   - 结果：39900

3. **三角形判断** → `03_triangle.py`
   - 边长输入 → 存在性判断 → 类型判断
   - 支持等边、等腰、等腰直角、直角、普通三角形

4. **简单计算器** → `04_calculator.py`
   - 异常处理 + match-case + 除零保护

## 关键收获

- `range(a, b)` 是左闭右开区间 `[a, b)`
- `exit()` 结束整个程序，`break` 只结束循环
- 列表用 `[]`，`append()` 添加元素
- 解包赋值 `a, b, c = [1, 2, 3]`
```

## 2026.04.20
## Python 列表与循环综合练习

**My Python Learning Journey (我的 Python 学习之路)**

转码预备役 | 记录从零开始系统学习 Python

---

## 📚 今日学习内容

| 知识点 | 练习题目 | 状态 |
|:---|:---|:---:|
| 嵌套循环 | 长方形打印、99乘法表 | ✅ |
| 循环控制 | `break`、`continue`、`exit()` | ✅ |
| 登录验证逻辑 | `while True` + 条件判断 | ✅ |
| 异常处理 | `try-except` 捕获输入错误 | ✅ |
| 随机数生成 | 猜数字游戏 | ✅ |
| 列表切片 | `s[1:5:2]` | ✅ |
| 列表增删改查 | `append`、`insert`、`pop`、`remove` | ✅ |
| 列表排序 | `sort()`、`reverse()`、`key=len` | ✅ |
| 列表合并 | `+`、`[*a,*b]`、`extend()` | ✅ |
| 列表去重 | 遍历 + `in` 判断 | ✅ |
| 数据统计 | 最大值、最小值、平均值 | ✅ |

---

## 💻 代码示例

### 1. 长方形打印

```python
try:
    a = int(input("请输入长方形的宽："))
    b = int(input("请输入长方形的长："))
except ValueError:
    print("请输入整数！！！")
    exit()

for i in range(a):
    for j in range(b):
        print("*", end="")
    print()
```

### 2. 99乘法表

```python
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={i * j}", end=" ")
    print()
```

### 3. 登录验证系统（优化版）

```python
while True:
    name = input("请输入账号：")
    key = input("请输入密码：")

    if name == "" or key == "":
        print("账号或密码不能为空！！！")
        continue

    valid = ((name == "admin" and key == "666888") or
             (name == "zhangsan" and key == "123456") or
             (name == "taoge" and key == "888666"))

    if not valid:
        print("账号或密码错误，请重新输入！！！")
        continue
    else:
        print("登录成功，进入B站首页~")
        break
```

### 4. 猜数字游戏

```python
import random

random_number = random.randint(1, 100)

while True:
    try:
        user_num = int(input("请输入数字:"))
    except ValueError:
        print("您输入的格式有误！！！")
        continue
    
    if user_num > random_number:
        print("您输入的数字比实际数字更大")
    elif user_num < random_number:
        print("您输入的数字比实际数字更小")
    else:
        print("您输入的数字就是实际数字！！！")
        break
```

### 5. 列表操作综合

```python
s = [1, 22, 7, 33, 4, 4, 5]

# 切片
s1 = s[1:5:2]

# 增删改查
s.append(7)
s.reverse()
s.sort()
s.sort(reverse=True)
s.insert(2, 90)
s.pop(2)
s.remove(7)

# 按长度排序
b = ["111", "22", "1", "aaa"]
b.sort(key=len)
b.sort(key=len, reverse=True)
```

### 6. 10个数字的统计

```python
s = []

for i in range(10):
    s.append(int(input(f"请输入数字{i+1}:")))

s.sort(reverse=True)
print(s)

max_value = s[0]
min_value = s[-1]
average = sum(s) / len(s)
print(f"最大值:{max_value}, 最小值:{min_value}, 平均值:{average}")
```

### 7. 列表合并 + 排序 + 去重（三种方法）

```python
num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]

# 方法1：+ 拼接（最简洁）
num = num_list1 + num_list2

# 方法2：解包合并
num = [*num_list1, *num_list2]

# 方法3：extend（修改原列表）
num_list1.extend(num_list2)
num = num_list1

# 统一处理：排序 + 去重
num.sort()
num_new = []
for x in num:
    if x not in num_new:
        num_new.append(x)

print(num_new)
```

---

## 🧠 核心知识点总结

### 1. `break` vs `continue` vs `exit()`

| 关键字 | 作用 |
|:---|:---|
| `break` | 退出当前循环 |
| `continue` | 跳过本次循环，继续下一次 |
| `exit()` | 退出整个程序 |

**注意**：`break` 和 `continue` 只作用于最内层循环。

### 2. 列表操作返回值

| 操作 | 返回值 | 是否修改原列表 |
|:---|:---|:---|
| `lst.append(x)` | `None` | ✅ 修改 |
| `lst.insert(i, x)` | `None` | ✅ 修改 |
| `lst.pop(i)` | 被删除的值 | ✅ 修改 |
| `lst.remove(x)` | `None` | ✅ 修改 |
| `lst.sort()` | `None` | ✅ 修改 |
| `lst.reverse()` | `None` | ✅ 修改 |
| `lst + [x]` | 新列表 | ❌ 不修改 |
| `[*lst1, *lst2]` | 新列表 | ❌ 不修改 |

**重要记忆**：会修改原列表的方法通常返回 `None`，不能赋值给变量。

### 3. `pop()` vs `del`

| 方法 | 返回值 | 删除范围 |
|:---|:---|:---|
| `pop()` | 被删除的值 | 单个元素（默认最后一个） |
| `del` | 无 | 单个元素 / 切片 / 整个列表 |

### 4. 列表合并的三种方式

| 方法 | 代码 | 是否创建新列表 |
|:---|:---|:---|
| `+` 拼接 | `new = a + b` | ✅ 是 |
| 解包合并 | `new = [*a, *b]` | ✅ 是 |
| `extend()` | `a.extend(b)` | ❌ 否（修改 a） |

### 5. 列表去重（经典方法）

```python
result = []
for x in original_list:
    if x not in result:
        result.append(x)
```

### 6. `in` 运算符

```python
if num0 not in num_new:  # 判断元素是否在列表中
```

`in` 返回布尔值（`True`/`False`），是列表查找的常用方法。

---

## 🐛 今日 Debug 记录

| 错误 | 原因 | 解决方案 |
|:---|:---|:---|
| `IndexError` | 空列表用 `s[i]` 赋值 | 用 `append()` 添加元素 |
| `ValueError` | 输入非数字 | 用 `try-except` 捕获 |
| 随机数每次都变 | 随机数生成在循环内 | 移到循环外生成一次 |
| 登录验证空值漏检 | 密码错误后没检空值 | 用 `while True` + `continue` 统一处理 |
| `append()` 返回 `None` | 误以为返回新列表 | 单独一行使用，不赋值 |

---

## 📁 文件结构

```
Python-Learning-2026.04.20/
├── README.md
├── 01_rectangle.py         # 长方形打印
├── 02_multiplication.py    # 99乘法表
├── 03_login_system.py      # 登录验证系统
├── 04_guess_number.py      # 猜数字游戏
├── 05_list_operations.py   # 列表操作综合
├── 06_number_stats.py      # 10个数字统计
└── 07_list_merge_dedup.py  # 列表合并+排序+去重
```

---

## 🔄 后续计划

- [ ] 函数基础（定义、参数、返回值）
- [ ] 模块与包的导入
- [ ] 文件读写操作
- [ ] 面向对象基础（暂缓）

---

## 📖 参考资料

- [Python 官方文档](https://docs.python.org/3/)
- [廖雪峰 Python 教程](https://www.liaoxuefeng.com/wiki/1016959663602400)

---

## 2026.04.22
## Python 列表推导式、字符串操作、元组与数据嵌套实战

**My Python Learning Journey (我的 Python 学习之路)**

转码预备役 | 记录从零开始系统学习 Python

---

## 📚 今日学习内容

| 知识点 | 练习题目 | 状态 |
|:---|:---|:---:|
| 列表推导式 | 生成平方列表、条件筛选 | ✅ |
| 字符串操作 | `find()`、`count()`、`upper()`、`split()`、`strip()`、`replace()` | ✅ |
| 邮箱格式验证 | `count()` + `in` 运算符 | ✅ |
| 元组定义 | 单元素元组需要逗号 | ✅ |
| 元组组包与解包 | `a,b,c = 100,200,300` | ✅ |
| 元组嵌套 | 学生成绩表 | ✅ |
| 数据统计 | 总分、平均分、最高/最低分 | ✅ |
| `\t` 制表符 | 表格对齐 | ✅ |

---

## 💻 代码示例

### 1. 列表推导式

```python
# 生成1-20的平方列表
num_list = [i**2 for i in range(1, 21)]
print(num_list)

# 从列表中提取偶数并计算平方
num_list = [19, 23, 54, 64, 87, 20, 109, 232, 123, 43, 26, 55, 72]
num_list2 = [i**2 for i in num_list if i % 2 == 0]
print(num_list2)

# 提取正数
list1 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]
list2 = [i for i in list1 if i > 0]
print(list2)
```

### 2. 字符串常用操作

```python
s = "python"

# 查找子串
print(s.find("th"))   # 2（索引位置）

# 统计次数
print(s.count("t"))   # 2

# 大小写转换
print(s.upper())      # PYTHON
print(s.lower())      # python

# 分割字符串
print(s.split("t"))   # ['py', 'hon']

# 去除指定字符
print(s.strip("p"))   # ython

# 替换子串
print(s.replace("p", "o"))  # oython

# 检查开头
print(s.startswith("py"))   # True

# 检查存在
print("th" in s)      # True
```

### 3. 邮箱格式验证

```python
email = input("请输入邮箱：")
if email.count("@") == 1 and "." in email:
    print("邮箱格式输入正确")
else:
    print("邮箱格式输入错误")
```

### 4. 元组组包与解包

```python
# 组包：把多个值打包成元组
a, b, c = 100, 200, 300
print(a, b, c)  # 100 200 300

# 交换变量（解包）
c, a, b = a, b, c
print(a, b, c)  # 200 300 100

# 单元素元组必须有逗号
t1 = (100,)   # ✅ 元组
t2 = (100)    # ❌ 整数
```

### 5. 学生成绩分析（元组嵌套实战）

```python
students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李木碗", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周铁", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐利果", 75, 69, 82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "遁天", 66, 59, 72),
)

# 打印表格（使用 \t 对齐）
print("学号\t姓名\t语文\t数学\t英语\t总分\t平均分")

for stu_id, name, chinese, math, english in students:
    total = chinese + math + english
    avg = total / 3
    print(f"{stu_id}\t{name}\t{chinese}\t{math}\t{english}\t{total}\t{avg:.1f}")

# 统计各科最高/最低分
chinese_scores = [s[2] for s in students]
math_scores = [s[3] for s in students]
english_scores = [s[4] for s in students]

print(f"语文：最高{max(chinese_scores)}，最低{min(chinese_scores)}")
print(f"数学：最高{max(math_scores)}，最低{min(math_scores)}")
print(f"英语：最高{max(english_scores)}，最低{min(english_scores)}")

# 找出平均分大于90的学生
for stu_id, name, chinese, math, english in students:
    if (chinese + math + english) / 3 > 90:
        print(f"{name}是优秀学生")
```

---

## 🧠 核心知识点总结

### 1. 列表推导式语法

```python
# 基础语法
[表达式 for 变量 in 可迭代对象]

# 带条件
[表达式 for 变量 in 可迭代对象 if 条件]

# 示例
[i**2 for i in range(1, 21)]                    # 平方列表
[i for i in list1 if i > 0]                     # 筛选正数
[i**2 for i in num_list if i % 2 == 0]          # 偶数平方
```

### 2. 字符串 vs 列表

| 特性 | 列表 | 字符串 |
|:---|:---|:---|
| 可变性 | ✅ 可变 | ❌ 不可变 |
| 修改操作 | 修改原列表，返回 `None` | 返回新字符串 |
| 典型操作 | `append()`、`pop()`、`sort()` | `upper()`、`replace()`、`split()` |

### 3. 元组要点

```python
# 定义
t = (1, 2, 3)           # 元组
t = (100,)              # 单元素元组（必须有逗号）
t = 100, 200, 300       # 不加括号也可以

# 只有两种查询操作
t.index(100)   # 查找位置
t.count(100)   # 统计次数

# 组包与解包
a, b, c = 100, 200, 300      # 组包
c, a, b = a, b, c            # 解包交换
```

### 4. 字符串常用方法

| 方法 | 作用 | 返回值 |
|:---|:---|:---|
| `s.find(sub)` | 查找子串 | 索引（找不到返回-1） |
| `s.count(sub)` | 统计次数 | 整数 |
| `s.upper()` | 转大写 | 新字符串 |
| `s.lower()` | 转小写 | 新字符串 |
| `s.split(sep)` | 分割 | 列表 |
| `s.strip(chars)` | 去除两端字符 | 新字符串 |
| `s.replace(old, new)` | 替换 | 新字符串 |
| `s.startswith(prefix)` | 检查开头 | `True`/`False` |
| `sub in s` | 检查存在 | `True`/`False` |

### 5. `\t` 制表符

- 作用：对齐文本，跳到下一个制表位
- 常用场景：打印表格、对齐多列数据
- 与空格的区别：自动对齐，不受内容长度影响

---

## 🐛 今日易错点

| 易错点 | 正确理解 |
|:---|:---|
| `(100)` 是元组吗？ | ❌ 不是，是整数。元组需要逗号 `(100,)` |
| 字符串方法修改原字符串？ | ❌ 不修改，返回新字符串 |
| `s.find()` 找不到返回什么？ | 返回 `-1`（不报错） |
| 列表推导式 `if` 放哪里？ | 放在 `for` 后面 |

---

## 📁 文件结构

```
Python-Learning-2026.04.22/
├── README.md
├── 01_list_comprehension.py   # 列表推导式
├── 02_string_operations.py    # 字符串操作
├── 03_email_validate.py       # 邮箱验证
├── 04_tuple_pack_unpack.py    # 元组组包解包
└── 05_student_scores.py       # 学生成绩分析
```

---

## 🔄 后续计划

- [ ] 字典与集合操作
- [ ] 函数基础（定义、参数、返回值）
- [ ] 文件读写操作

---

## 📖 参考资料

- [Python 官方文档](https://docs.python.org/3/)
- [廖雪峰 Python 教程](https://www.liaoxuefeng.com/wiki/1016959663602400)

---

# 📝 今日学习README日志

## 📅 日期：2026年4月24日

---

## 一、今日重点掌握的知识点

### 1. 集合（set）
- **特点**：无序、不可重复、可修改
- **重要方法**：
  - `pop()`：删除随机元素并返回被删除的元素
  - 交并差运算：返回新集合（加 `_update` 会修改原集合返回空值）
- **注意**：定义空集合只能用 `set()`，不能用 `{}`（那是空字典）

### 2. 字典（dict）
- **特点**：存储键值对（key:value）类型数据
- **核心规则**：
  - ✅ value可以是任何类型数据
  - ❌ key不能为可变类型（列表、集合、字典）
  - key重复时，后面的值会覆盖前面的值

### 3. 字典的三种遍历方式
```python
# 方式1：按键遍历
for k in dict1.keys():
    print(f"{k} : {dict1[k]}")

# 方式2：按值遍历
for v in dict1.values():
    print(v)

# 方式3：按键值对遍历（解包）
for k, v in dict1.items():
    print(f"{k} : {v}")
```

---

## 二、今日解决的关键问题

### 问题1：添加功能逻辑错误
**原问题**：商品添加语句放在判断条件内部，导致用户输入"否"时商品不会被添加

**解决方案**：
- 先执行添加操作，再询问是否继续
- 调整代码执行顺序，确保商品必定被添加

### 问题2：退出系统功能缺失
**原问题**：用户无法正常退出程序，只能强制关闭

**解决方案**：
- 在首页菜单添加退出选项（输入数字6退出）
- 使用 `break` 跳出外层循环，正常结束程序

### 问题3：`dict_keys` 对象显示不友好
**原问题**：`gwc.keys()` 返回 `dict_keys(['香蕉', '橙子'])`，不够直观

**解决方案**：
- 使用 `list(gwc.keys())` 转换为列表
- 提升可读性，便于用户查看

---

## 三、今日完成的代码项目

### 🛒 购物车管理系统（完整版）

**功能清单**：
- ✅ 增加商品（含异常处理）
- ✅ 修改商品（含存在性检查）
- ✅ 删除商品（含安全校验）
- ✅ 查询商品（含空购物车提示）
- ✅ 返回上一级菜单
- ✅ 退出系统

**技术要点**：
```python
# 异常处理
try:
    price = float(input("请输入商品价格："))
except ValueError as e:
    print(f"格式错误：{e}")

# 字典操作
gwc[name] = (price, quantity)  # 添加/修改

# 存在性检查
if name in gwc:
    del gwc[name]

# 遍历输出
for k, v in gwc.items():
    print(f"商品名称：{k}，价格：{v[0]}，数量：{v[1]}")
```

---

## 四、代码优化记录

| 问题类型 | 优化前 | 优化后 |
|---------|--------|--------|
| 添加逻辑 | 先询问后添加 | 先添加后询问 |
| 退出功能 | 无退出选项 | 输入6退出系统 |
| 键的显示 | `dict_keys(['苹果'])` | `list(gwc.keys())` → `['苹果']` |
| 异常处理 | 部分功能缺失 | 所有输入都有异常捕获 |

---

## 五、今日总结

**重要收获**：
1. 集合和字典的核心特性及使用场景
2. 字典的三种遍历方式及适用场景
3. 循环嵌套中 `break` 和 `continue` 的正确使用
4. 异常处理让程序更加健壮

**一句话总结**：
> 掌握了集合与字典的核心用法，并通过购物车管理系统实战，深入理解了增删改查的实现逻辑和异常处理的重要性。

---

## 六、明日计划

- [ ] 学习文件操作（保存购物车数据）
- [ ] 理解函数封装，优化代码结构
- [ ] 尝试添加商品总价计算功能

---

*今日代码已全部测试通过，运行正常！* ✅

## 2026.04.26
## Python 函数核心知识点总结

**My Python Learning Journey (我的 Python 学习之路)**

转码预备役 | 记录从零开始系统学习 Python

---

## 📚 今日学习内容

| 知识点 | 状态 | 核心要点 |
|:---|:---:|:---|
| 函数定义与调用 | ✅ | 先定义后调用，形参与实参 |
| 函数嵌套调用 | ✅ | 栈结构（后进先出） |
| 全局变量与局部变量 | ✅ | `global` 声明，作用域区别 |
| 参数传递方式 | ✅ | 位置参数 → 关键字参数 |
| 不定长参数 | ✅ | `*args`（元组）、`**kwargs`（字典） |
| 函数作为参数 | ✅ | 高阶函数基础 |
| 匿名函数 | ✅ | `lambda` 表达式 |
| 递归函数 | ✅ | 函数调用自身，栈的思维 |
| 类型注解 | ✅ | `参数: 类型`、`-> 返回值类型` |

---

## 🧠 核心知识点

### 1. 全局变量与局部变量

```python
num = 1  # 全局变量

def test():
    local_var = 10      # 局部变量，函数结束后销毁
    global num2         # 声明全局变量（只能声明，不能赋值）
    num2 = num + 1      # 修改全局变量
    return local_var

test()
print(num2)     # ✅ 2
# print(local_var)  # ❌ 局部变量外部不可访问
```

| 变量类型 | 作用域 | 生命周期 | 声明方式 |
|:---|:---|:---|:---|
| 全局变量 | 整个模块 | 程序运行期间 | 函数外直接定义 |
| 局部变量 | 函数内部 | 函数调用期间 | 函数内直接定义 |
| 全局变量（函数内修改） | 整个模块 | 程序运行期间 | `global x` |

---

### 2. 参数传递规则

```python
def func(a, b, c=0, *args, **kwargs):
    print(a, b, c, args, kwargs)

# 规则：位置参数 → 关键字参数 → *args → **kwargs
func(1, 2, 3, 4, 5, name="张三", age=18)
# a=1, b=2, c=3, args=(4,5), kwargs={'name':'张三','age':18}
```

| 参数类型 | 写法 | 打包类型 | 调用方式 |
|:---|:---|:---|:---|
| 位置参数 | `a, b` | - | `func(1, 2)` |
| 默认参数 | `c=0` | - | `func(1, 2)` 或 `func(1, 2, 3)` |
| 不定长位置 | `*args` | 元组 | `func(1, 2, 3, 4, 5)` |
| 不定长关键字 | `**kwargs` | 字典 | `func(1, 2, name="张三")` |

**混用规则**：位置参数 → 关键字参数 → `*args` → `**kwargs`

---

### 3. 递归函数

```python
def factorial(n):
    if n == 0:          # 递归结束条件（必须）
        return 1
    return n * factorial(n - 1)  # 调用自身

print(factorial(5))  # 120
```

**递归的栈逻辑**：
```
factorial(5) 压栈
  → factorial(4) 压栈
    → factorial(3) 压栈
      → factorial(2) 压栈
        → factorial(1) 压栈
          → factorial(0) 压栈 → 返回 1
        ← 返回 1 * 1 = 1
      ← 返回 2 * 1 = 2
    ← 返回 3 * 2 = 6
  ← 返回 4 * 6 = 24
← 返回 5 * 24 = 120
```

| 与 while 循环 | 关系 |
|:---|:---|
| 任何递归都能改写成 while | ✅ |
| 任何 while 都能改写成递归 | ✅ |
| Python 递归深度限制 | 默认 1000 |

---

### 4. 匿名函数（lambda）

```python
# 传统函数
def add(x, y):
    return x + y

# lambda 表达式（相同功能）
add2 = lambda x, y: x + y

print(add(3, 4))    # 7
print(add2(1, 2))   # 3
```

**语法**：`lambda 参数: 表达式`

| 特点 | 说明 |
|:---|:---|
| 不需要 `return` | 表达式结果自动返回 |
| 不能换行 | 只能写单行表达式 |
| 通常用作参数 | 高阶函数常用 |

---

### 5. 类型注解

```python
# 变量类型注解
a: int = 695
names: list[str] = ["A", "C", "E"]
options: dict[str, int] = {"count": 2, "total": 10}

# 函数类型注解
def process(data: tuple[str, float, int], coupon: int = 0) -> tuple[int, int, float]:
    return (len(data[0]), int(data[1]), data[2] + 0.5)

# 多种可能类型
def parse(x: int | float | str) -> int | None:
    return int(x) if str(x).isdigit() else None
```

| 注解位置 | 语法 | 示例 |
|:---|:---|:---|
| 参数 | `参数名: 类型` | `scores: list[int]` |
| 返回值 | `-> 类型` | `-> bool` |
| 多种类型 | `\|`（Python 3.10+） | `int \| float` |

**注意**：类型注解**不影响运行**，只提供 IDE 提示和代码可读性。

---

## 🐛 今日易错点

| 易错点 | 正确理解 |
|:---|:---|
| `global num = 5` | ❌ `global` 只能声明，不能赋值 |
| `*args: tuple[str,int]` | ❌ `*args` 不能这样限制固定长度 |
| 局部变量外部访问 | ❌ 函数调用后局部变量销毁 |
| 参数顺序 | 位置参数必须在关键字参数前 |
| 递归无结束条件 | ❌ 会无限递归导致栈溢出 |

---

## 📁 代码示例

### 商品价格计算（不定长参数 + 默认参数）

```python
def goods_test(*args, coupon=0, score=0, express=0.0):
    """
    计算商品最终价格
    args: (商品名, 价格, 数量) 的元组
    """
    # 计算总价
    total = sum(goods[1] * goods[2] for goods in args)
    
    # 扣减优惠券
    if total >= 5000:
        total -= coupon
    
    # 积分抵扣（每100积分抵扣1元）
    if total >= 5000:
        total -= score // 100
    
    return total + express

# 调用
result = goods_test(("电脑", 6000, 1), ("手机", 2000, 1), 
                    coupon=2000, score=100, express=73.5)
print(result)  # 6173.5
```

---

## 🔄 后续计划

- [ ] 数据结构与算法（数组、链表、栈、队列）
- [ ] LeetCode 刷题
- [ ] 面向对象基础（暂缓）

---

## 📖 参考资料

- [Python 官方文档](https://docs.python.org/3/)
- [廖雪峰 Python 教程](https://www.liaoxuefeng.com/wiki/1016959663602400)

---

## 2026.04.29
## Python 模块与包核心知识点

**My Python Learning Journey (我的 Python 学习之路)**

转码预备役 | 记录从零开始系统学习 Python

---

## 📚 今日学习内容

| 知识点 | 状态 | 核心要点 |
|:---|:---:|:---|
| 模块 (module) | ✅ | `.py` 文件，代码组织的基本单位 |
| 包 (package) | ✅ | 文件夹 + `__init__.py`，模块的集合 |
| `__all__` | ✅ | 控制 `import *` 的功能范围 |
| `__name__` | ✅ | `"__main__"`（直接运行）或模块名（被导入） |
| `if __name__ == "__main__"` | ✅ | 防止导入时执行测试代码 |
| 常量命名规范 | ✅ | 全大写，约定不可修改 |
| 模块导入方式 | ✅ | `import`、`from...import`、`import...as` |

---

## 🧠 核心知识点

### 1. 模块 (Module)

**模块就是一个 `.py` 文件**，把相关功能放在一起。

```python
# module4291.py
PI = 3.14
NAME = "SSR"

def m1():
    print("-" * 60)

def m2():
    print("*" * 60)

def m3():
    print("#" * 60)
```

### 2. 导入模块的几种方式

```python
# 方式1：导入整个模块
import module4291
print(module4291.PI)
module4291.m1()

# 方式2：导入特定功能
from module4291 import PI, m1
print(PI)
m1()

# 方式3：导入并起别名
import module4291 as m
print(m.PI)

# 方式4：导入所有（不推荐，受 __all__ 限制）
from module4291 import *
```

### 3. `__all__`：控制 `import *` 的范围

```python
# 在模块中定义 __all__
__all__ = ["NAME", "m1", "m2"]  # 只有 NAME, m1, m2 能被 `import *` 导入

PI = 3.14      # ❌ 不会被导入
NAME = "SSR"   # ✅ 会被导入

def m1(): pass # ✅ 会被导入
def m2(): pass # ✅ 会被导入
def m3(): pass # ❌ 不会被导入
```

| `__all__` | 作用 |
|:---|:---|
| 定义时 | 指定 `import *` 能导入哪些功能 |
| 未定义时 | `import *` 导入所有非下划线开头的功能 |

### 4. `__name__`：当前模块的名字

```python
# 直接运行当前文件时
print(__name__)  # "__main__"

# 被其他文件导入时
print(__name__)  # "module4291"（模块名）
```

### 5. `if __name__ == "__main__"` 的经典用法

```python
# module4291.py
def m1():
    print("功能代码")

# 测试代码（只在直接运行时执行）
if __name__ == "__main__":
    m1()           # 测试代码
    print("测试中...")
```

| 运行方式 | `__name__` | 测试代码是否执行 |
|:---|:---|:---|
| 直接运行 | `"__main__"` | ✅ 执行 |
| 被导入 | 模块名 | ❌ 不执行 |

**作用**：让模块既能作为工具库被导入，又能作为独立程序测试运行。

### 6. 包 (Package)

**包是一个包含 `__init__.py` 文件的文件夹**，用于组织多个模块。

```
my_package/                    # 包
├── __init__.py                # 标识这是包
├── utils.py                   # 模块
└── math.py                    # 模块
```

```python
# 导入包中的模块
from my_package import utils
from my_package.utils import m1
```

### 7. `__init__.py` 的作用

```python
# __init__.py
__all__ = ["utils", "math"]    # 控制 from package import * 的导入
```

| 功能 | 说明 |
|:---|:---|
| 标识文件夹是否为包 | 必须存在（Python 3.3+ 非必须，但建议保留） |
| 控制 `import *` | 通过 `__all__` 指定 |
| 包的初始化代码 | 可以在其中写代码 |

---

## 🐛 今日易错点

| 易错点 | 正确理解 |
|:---|:---|
| `import *` 会导入所有 | ❌ 受 `__all__` 限制 |
| 包和文件夹没区别 | ❌ 包需要 `__init__.py` |
| 常量全大写后可修改 | ⚠️ 只是约定，Python 不强制 |
| 测试代码不写 `if __name__` | ❌ 导入时会自动执行测试代码 |

---

## 📁 代码示例

### 模块文件：`module4291.py`

```python
# 常量（全大写，约定不可修改）
PI = 3.14
NAME = "SSR"

# __all__ 控制 import * 的范围
__all__ = ["NAME", "m1", "m2"]

def m1():
    print("-" * 60)

def m2():
    print("*" * 60)

def m3():
    print("#" * 60)

# 测试代码（只在直接运行时执行）
if __name__ == "__main__":
    m1()
    m2()
    m3()
```

### 使用模块：`main.py`

```python
# 方式1：导入特定功能
from module4291 import PI, NAME, m1, m2

print(PI)    # 3.14
print(NAME)  # SSR
m1()         # ------------------------------------------------------------
m2()         # ************************************************************

# 方式2：import *（受 __all__ 限制）
from module4291 import *  # 只能导入 NAME, m1, m2
# PI 和 m3 无法使用
```

---

## 💡 核心总结

| 概念 | 定义 | 关键点 |
|:---|:---|:---|
| **模块** | `.py` 文件 | 代码组织的基本单位 |
| **包** | 文件夹 + `__init__.py` | 模块的集合 |
| `__all__` | 列表 | 控制 `import *` 的导出内容 |
| `__name__` | 字符串 | 直接运行 = `"__main__"`，被导入 = 模块名 |
| `if __name__ == "__main__"` | 条件语句 | 阻止导入时执行测试代码 |

---

## 🔄 后续计划

- [ ] 数据结构与算法（数组、链表、栈、队列）
- [ ] LeetCode 刷题
- [ ] 面向对象基础（暂缓）

---

## 📖 参考资料

- [Python 官方文档 - Modules](https://docs.python.org/3/tutorial/modules.html)
- [廖雪峰 Python 教程 - 模块](https://www.liaoxuefeng.com/wiki/1016959663602400/1017454145014176)

---

*持续更新中...* 🚀
