# @Author  :  comma 
# @Date    :  2020-12-01 21:32

'''
Queue是线程安全的队列，在使用时无需加锁，可以在多线程中直接使用。
队列也是实现线程间同步的方式
FIFO(先进先出)队列Queue
LIFO(后进先出)LifoQueue
qsize() 返回队列的大小
empty() 判断队列是否为空
full() 判断队列是否满了
get() 从队列中取最先插入的数据
put() 将一个数据放到队列中
'''
from queue import Queue  # FIFO，先进先出队列
import random
import time
import threading

def demo():
    q=Queue(5)# 创建一个队列，最多可以存放5个数据
    for i in range(4):
        q.put(i)
    print('队列中实际数据是：',q.qsize())

    for _ in range(5):
        try:
            print(q.get(block=False))
        except:
            print('数据已经取完，目前队列为空')
            break

def add_value(q):
    while True:
        q.put(random.randint(100, 1000))
        time.sleep(1)


def get_value(q):
    while True:
        print('取出了元素{}'.format(q.get()))


def start():
    q = Queue(10)
    t1 = threading.Thread(target=add_value, args=(q,))
    t2 = threading.Thread(target=get_value, args=(q,))
    t1.start()
    t2.start()


if __name__ == '__main__':
    # start()
    demo()
