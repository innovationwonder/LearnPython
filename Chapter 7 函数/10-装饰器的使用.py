def new_tips(argv):
    def tips(func):
        def nei(a,b):
            print('开始 %s' %argv)
            func(a,b)
            print('结束 %s' %func.__name__)

        return nei
    return tips


# @tips
# def add(a,b):
#     print(a+b)
#
# print(add(2,3))


@new_tips("sub_module")
def sub(a,b):
    print(a-b)

sub(5,4)