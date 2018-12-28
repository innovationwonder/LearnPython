import threading
from threading import current_thread
import time

def mythread(a,b):
    print(current_thread().getName(), 'start')
    print('%s %s' %(a,b))
    time.sleep(1)
    print(current_thread().getName(), 'stop')

for i in range(1,6):
    # t = mythread(i,i+1)
    t1 = threading.Thread(target=mythread, args=(i, i+1))
    t1.start()

print(current_thread().getName(),'end')