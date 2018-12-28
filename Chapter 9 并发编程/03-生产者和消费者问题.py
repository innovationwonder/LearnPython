from threading import Thread, current_thread
import time
import random
from queue import Queue


q = Queue(5) # 定义队列长度


# 生产者：经过随机休眠时间向队列中添加数字
class ProduceThread(Thread):
    def run(self):
        name = current_thread().getName()
        nums = range(100)
        global q
        while True:
            num = random.choice(nums) # 从序列中随机选择一个数字
            q.put(num) # 向队列里添加数字
            print('生产者生产了 %s 数据 %s' %(name, num))
            t = random.randint(1,3) # 产生一个 1~3 中一个整数型随机数
            time.sleep(t)
            print('生产者 %s 睡眠了 %s' %(name, t))


# 消费者：经过随机休眠时间从队列中提取数字
class ConsumerThread(Thread):
    def run(self):
        name = current_thread().getName()
        global q
        while True:
            num = q.get() # 从队列中取数字
            q.task_done() # 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
            print('消费者 %s 消耗了数据 %s' %(name, num))
            t = random.randint(1,5)
            time.sleep(t)
            print('消费者 %s 睡眠了 %s' %(name, t))


p1 = ProduceThread(name='p1')
p1.start()

p2 = ConsumerThread(name='p2')
p2.start()