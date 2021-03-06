# 内部函数引用外部变量 -- 闭包
def func():
    a = 1
    b = 2
    return a + b

def sum(a):
    def add(b):
        return a + b
    return add

# add 函数的名称或引用
# add() 函数的调用

num1 = func()

num2 = sum(2)

print(type(num1))
print(num2)

print('计数器--------------------')


def counter(first=0):
    cnt = [first]

    def add_one():
        cnt[0] += 1
        return cnt[0]

    return add_one


num5 = counter(5)
print(num5())
num10 = counter(10)
print(num10())