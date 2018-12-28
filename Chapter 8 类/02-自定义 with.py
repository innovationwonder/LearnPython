class Testwith():
    def __enter__(self):
        print('run')

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print('exit')
        if exc_tb is None:
            print('正常运行')
        else:
            print('has error is %s' %exc_tb)

with Testwith():
    print('Test is running')
    raise NameError('测试异常')