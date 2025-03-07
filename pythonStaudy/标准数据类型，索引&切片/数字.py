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