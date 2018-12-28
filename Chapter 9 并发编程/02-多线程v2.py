import threading
from threading import current_thread

# 实现主线程结束后，子线程再结束
class Mythread(threading.Thread):
    def run(self):
        print(current_thread().getName(), 'start')
        print('run')
        print(current_thread().getName(), 'stop')


t1 = Mythread()
t1.start()
t1.join()

print(current_thread().getName(), 'end')