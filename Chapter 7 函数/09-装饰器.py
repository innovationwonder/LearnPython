import time


# print(time.time())
# time.sleep(1)


def timmer(func):
    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print('程序运行了 %s s' % (stop_time - start_time))
    return wrapper


@timmer
def process_time():
    time.sleep(3)

process_time()

# start_time = time.time()
# process_time()
# stop_time = time.time()
# print('程序运行了 %s s' %(stop_time-start_time))