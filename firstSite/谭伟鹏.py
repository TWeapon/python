# string = 'hello world', 如何切片可以输出 'hello w'?
string = 'hello world'
print(string[0: 7])
print(string[: 7])
print(string[-len(string): (len(string) - 1) - 3])
print(string[-len(string) - 100: (len(string) - 1) - 3])

# string = 'hello world', string[5:-1]的结果是什么?
#  worl
print(string[5:-1])

# string = 'hello world', string[1:9:2]的结果是什么?
# ello wor
# el o
print(string[1:9:2])

# string = 'hello world', string[-2:4:-2]的结果是什么?
# o worl
# lo
print(string[-2:4:-2])
# 给定时间字符串 t = "2025/02/28-14:35"，提取月份和分钟数并计算它们的乘积
t = "2025/02/28-14:35"
# 1 answer 通过分隔符
tMonth = t.split('/')[1]
tMinute = t.split('/')[2].split(':')[1]
print(fr"月份：{tMonth}，分钟数{tMinute}，二者乘积是：{int(tMonth) * int(tMinute)}")
tMonth = t.split('-')[0].split('/')[1]
tMinute = t.split('-')[1].split(':')[1]
print(fr"月份：{tMonth}，分钟数{tMinute}，二者乘积是：{int(tMonth) * int(tMinute)}")

# 2 answer 通过切片
tMonth = t[5:7]
tMinute = t[14:]
print(fr"月份：{tMonth}，分钟数{tMinute}，二者乘积是：{int(tMonth) * int(tMinute)}")

# 给定字符串 s = "12a3a4AA5A"，求出 'a' 字符和 'A' 字符的数量差
s = "12a3a4AA5A"
aCount = s.count('a')
ACount = s.count('A')
dif = aCount - ACount if aCount > ACount else ACount - aCount
print(
    fr"a数量：{aCount}，A数量：{ACount}，'a' 字符和 'A' 字符的数量差为：{dif}")

"""
编写一个程序, 帮助水果店实现计价功能:
请用户输入水果品种, 水果单价(元/kg)和重量(kg),
计算出需要花费的金额并做格式化输出

例:
用户输入水果品种为: 苹果
输入单价为: 3.98
输入重量为: 2.58
根据用户输入数据计算出总价为: 10.2684

请用三种字符串格式化方式输出如下结果:
您购买了2.58kg的苹果, 单价为3.98元/kg, 您需要支付10.27元!
"""

fruitVariety = input("请输入水果品种:")
unitPrice = float(input("请输入单价:"))
weight = float(input("请输入重量:"))
print("######################################")
print("用户输入水果品种为: %s" % fruitVariety)
print("输入单价为: %.2f" % unitPrice)
print("输入重量为: %.2f" % weight)
totalPrice = unitPrice * weight
print("根据用户输入数据计算出总价为: %f" % totalPrice)
print("######################################")
# %格式化
print("您购买了%.2fkg的%s, 单价为%.2f元/kg, 您需要支付%.2f元!" % (weight, fruitVariety, unitPrice, totalPrice))
# format格式化
print("您购买了{:.2f}kg的{}, 单价为{:.2f}元/kg, 您需要支付{:.2f}元!".format(weight, fruitVariety, unitPrice, totalPrice))
# f-string格式化
print(f"您购买了{weight:.2f}kg的{fruitVariety}, 单价为{unitPrice:.2f}元/kg, 您需要支付{totalPrice:.2f}元!")
