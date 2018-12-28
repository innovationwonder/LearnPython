'''
练习一 文件的创建和使用
创建一个文件，并写入当前日期
再次打开这个文件，读取文件的前4个字符后退出
'''
import datetime
now = datetime.datetime.now()
with open('time_now','w') as f:
    # 注意write( )方法写入的内容是字符串类型
    f.write(str(now))

with open('time_now') as f:
    a = f.read(4)
    print(a)
