# os.path
import os
a = os.path.abspath('.') # 获取当前目录
b = os.path.abspath('..') # 获取上一级目录
print(a)
print(os.path.exists('/Develop')) # 判断根目录下此目录是否存在
print(os.path.isfile('/Develop')) # 判断是否是文件
print(os.path.isdir('/Develop')) # 判断是否是目录

os.path.join('a/n/v','vc/fd') # 连接路径

from pathlib import Path
p = Path('.')
print(p.resolve()) # 获取当前目录

p.is_dir()

# 新建目录
