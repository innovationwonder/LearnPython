# re 模块 功能：使用正则表达式对字符进行匹配和搜索
# . 匹配任意单个字符
# ^ 以某个字符开头 $ 以某个字符结束
# * 匹配前面的字符出现 0/x 次  + 前面的字符出现 1/x 次  ？ 前面的字符出现 0/1 次
# {m} 表示前面的字符出现m次 {m,n} 前面的字符出现 m 次 ~ n 次
# [abcd] 表示其中任一个字符出现
# | 前者或者后者
# \d == [0-9]+  \D 匹配不包含数字
# \s
# ()
# ^$ 表示一行为空行
# .*? 不使用贪婪模式
import re

# 匹配 match() 用于完全匹配进行分组
p = re.compile(r'(\d+)-(\d+)-(\d+)')
# print(p.match('2018-7-10').group(1))

year, month, day = p.match('2018-7-10').groups()
print(year, month, day)

# 搜索功能 serach() 返回第一个 查找  findall() 搜索全部
print(p.search('aa018-7-10'))

# 替换 sub(a, b, c)  a 为匹配规则  b 为替换上的字符， c 为被替换的字符
phone_number = '410-5541-7456'
p3 = re.sub(r'\D',' ',phone_number)
print(p3)