# int([x],base=10)
# x:数字或字符串
# base:进制数，默认十进制（当base传参时，x必须为字符串）
# 将x转换为十进制整数并返回，如果没有指定x,则返回0
print(int())  # 0
print(int(3.99))  # 3
print(int("12"))  # 12

# ValueError: 字符串中包含了一个小数点，无法被解释为整数
# print(int("12.1"))

# 将二进制的“101010”转为十进制的整数
print(int("101010", base=2))  # 42
print(int("0b101010", 2))  # 42
# 将八进制的“11”转为十进制的整数
print(int("11", base=8))  # 9
print(int("0o11", base=8))  # 9
# 将十六进制的“3d”转为十进制的整数
print(int('3d', base=16))  # 61
print(int("0x3d", base=16))

# bin(x)/ oct(x) / hex(x)
# 返回整数类型的二进制表示形式（前缀为“0b”）
# 返回整数类型的八进制表示形式（前缀为“0o”）
# 返回整数类型的十六进制表示形式（前缀为“0x”）
num = 47
print(bin(num))  # '0b101111'
print(oct(num))  # '0o57'
print(hex(num))  # '0x2f'
print(int("0b101111", base=2))
print(int("0o57", base=8))
print(int("0x2f", base=16))

# float([x])
# x:数字或字符串
# 将x转换成浮点数并返回，不指定x,则返回0.0
print(float())  # 0.0
print(float(123))  # 123.0
print(float('123'))  # 123.0
print(float('1.23'))  # 1.23
print(float('3.99'))  # 3.99
print(float('-3.99'))  # -3.99
print(float(True))  # 1.0
print(float(False))  # 0.0

# bool([x])
# 根据指定的x,返回布尔值
# 如果没有指定x,则返回False
"""
数字0,0.0,0j,False,
空字符串,空列表,空元组,
空字典,空集合,关键字None
...
以上这些数据bool判定为False
其它通常判定为True
"""
print(bool())  # False
print(bool(0))  # False
print(bool(0.0))  # False
print(bool(0.0))  # False
print(bool(0j))  # False
print(bool(False))  # False
print(bool(''))  # False
print(bool([]))  # False
print(bool(()))  # False
print(bool({}))  # False
print(bool(set()))  # False
print(bool(None))  # False
print(bool(' '))  # True
print(bool('None'))  # True
print(bool('False'))  # True

# complex([real[, imag]])
# 返回一个real+imag*1j的复数
# 如果第一个参数是字符串，它将被解释为复数，此时不能传第二个参数
# 如果没有指定实参，则返回0j
print(complex())  # 0j
print(complex(3.2, 4))  # (3.2+4j)
print(complex(3.2))  # (3.2+0j)
print(complex('3.2'))  # (3.2+0j)
print(complex("3.2+4j"))  # (3.2+4j)

# 字符串（String）
# 特性：不可变，是序列
# 单行字符串：用一对单引号或一对双引号定义
# 多行字符串：用三个单引号或三个双引号定义
s1 = '这是一个单行字符串'
s2 = "这是一个单行字符串"
s3 = '''这是一个单行字符串'''
s4 = """这是一个单行字符串"""
print(s1, s2, s3, s4)
# str(object='')
# 返回object的字符串格式
print(str())  # '' 没有空格字符
print(str(1234))  # '1234'
print(str(-1.23))  # '-123'

# Raw 字符串
# 如果希望字符串中的转义字符不发生转义效果，可以在字符串前面加一个字母r，表示原始字符串

print(R'https:\\www.example.com\nuxy\tngj')

# %格式化
# %s 格式化为字符串
# %d、%i 格式化为十进制整数，仅适用于数字
# %f、%F 格式化为浮点数，默认精确到小数点后六位，仅适用于数字

print('它说它叫%s,今年%d岁,每天睡%f小时！' % ('旺财', 2, 8.5))
# %.nf 表示精确到小数点后n位
print('今天买了%s斤青菜，%s元/斤，花了%.2f元！' % (3.5, 2.59, 3.5 * 2.59))
# format方法格式化
name = '旺财'
age1 = 2
age2 = 3
# 传位置参数，实参按照从左往右的顺序传入占位符{}
print('它说它叫{}，它今年{}岁，它宝宝{}个月了！'.format(name, age1, age2))
# 传关键字参数
print('它说它加{n}，它今年{a1}岁，它宝宝{a2}个月了！'.format(a1=age1, n=name, a2=age2))
# 根据实参的下标传参
print('它说它叫{1}，它今年{0}岁，它宝宝{2}个月了！'.format(age1, name, age2))
# f-string格式化 *********
print(f'它说它加{name}，它今年{age1}岁，它宝宝{age2}个月了！')
print(fr'它说它加{name}，它今年{age1}岁，它宝宝{age2}个月了！')
# {value:.nf} 表示精确到小数点后n位
print(fr'今天买了{3.5}斤青菜，{2.59}元/斤，花了{3.5 * 2.59:.2f}元！')

# 字符串方法
# str.replace(old,new,count=-1)
# old:旧字符串
# new:新字符串
# count:要替换的最大次数，默认不限制替换次数
# 用新字符串替换旧字符串并返回
s = "Line1 Line2 Line4"
# 用“b”替换所有的“Li”
print(s.replace("Li", "b"))
print(s.replace("Li", "b", 2))

# str.strip([chars])
# chars:指定要移除的字符，如果没有指定，则默认移除空白字符（空格符，换行符，制表符）
# 删除字符串左右两边指定的字符

# 删除字符串左右两边指定的字符
str1 = ' \thello wrold h \n'
print(str1.strip())

# 删除字符串两边的‘o’字符
str2 = "ooho hello wrold"
print(str2.strip('o'))

# 删除字符串两边的‘c','w','o','m'
str3 = 'www.example.com'
print(str3.strip("cwom"))

# str.startswith(prefix[,start[,end]])
# prefix:匹配的前缀，可以是字符串或者字符串组成的元组（元组中只要一个元素满足即可）
# start:开始索引，不指定则默认为0
# end:结束索引（开区间），不指定则默认为len(str)
# 判定字符串是否以prefix指定的值开始（start和end参数用来控制字符串的判定区间）
str1 = "hello world"
print(str1.startswith("h"))
print(str1.startswith("he"))
print(str1.startswith("wo"))
print(str1.startswith("wo", 1, 3))
print(str1.startswith(("wo", "h")))  # 元组中只要一个元素满足即可
print('################################')
# str.endswith(suffix[,start[,end]])
# suffix:匹配的前缀，可以是字符串或者字符串组成的元组（元组中只要一个元素满足即可）
# start:开始索引，不指定则默认为0
# end:结束索引（开区间），不指定则默认为len(str)
# 判定字符串是否以suffix指定的值结束（start和end参数用来控制字符串的判定区间）
str1 = "hello world"
print(str1.endswith("d"))
print(str1.endswith("ld"))
print(str1.endswith("lo"))
print(str1.endswith("lo", 1, 5))    # 结尾是开区间
print(str1.endswith(("d", "lo")))  # 元组中只要一个元素满足即可
print('################################')
# str.isdigit()
# 判定字符串中的每个字符是否都为数字型的字符
string = '1234'  # true
print(string.isdigit())

string = '-1234'    # false
print(string.isdigit())

string = '1.234'    # false
print(string.isdigit())

