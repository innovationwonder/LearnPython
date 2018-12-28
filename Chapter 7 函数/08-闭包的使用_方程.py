# y = a * x + b


def line(a,b):
    def arg_y(x):
        return a*x+b
    return arg_y


def aline(a,b):
    c = lambda x: a*x+b
    return c


line2 = aline(3,1)
print(line2(2))

line1 = line(3,2)
print(line1(5))