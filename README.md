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
