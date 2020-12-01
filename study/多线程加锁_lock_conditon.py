# @Author  :  comma 
# @Date    :  2020-11-30 22:04
'''
线程常用方法：
    threading.current_thread()  : 获取当前线程对象
    threading.enumerate()   :获取当前运行的n多线程信息
    getName()   :获取线程的名称
    setName()   :设置线程名称

线程加锁步骤：
    创建锁对象： threading.Lock()
    加锁 ： .acquire()
    释放锁 : .release()

condition版的生产者与消费者模式
    acquire() : 上锁
    release() : 解锁
    wait()  : 将当前线程处于等待状态，并且会释放锁。可以被其它线程使用notify()和notify_all()函数唤醒。被唤醒后会继续等待上锁，上锁后继续执行下面的代码。
    notify() : 通知某个正等待的线程，默认是第一个等待的线程
    notify_all()  : 通知所有正在等待的线程。notify()和notify_all()需要在release()之前调用。
'''

import threading
import random

total_money = 0
lock = threading.Condition()
times=0 #统计次数


class Producer(threading.Thread):   # 生产者，赚钱
    def run(self):
        global total_money
        global times
        for _ in range(10):
            lock.acquire()  # 加锁
            money = random.randint(1000, 10000)
            total_money += money
            times+=1
            print(threading.current_thread().getName(), '挣了{}钱,当前余额为{}'.format(money, total_money))
            lock.notify_all()   # 唤醒所有等待的线程
            lock.release()  # 释放锁

class Customer(threading.Thread):   # 消费者，消费钱
    def run(self):
        global total_money
        for _ in range(10):
            lock.acquire()  # 上锁
            money=random.randint(1000,10000)
            while money>total_money:
                if times>=50:
                    lock.release()
                    return
                print(threading.current_thread().getName(),'想花{}钱，但是余额不足，当前余额为：{}'.format(money,total_money))
                lock.wait() # 等待挂起，余额不足需要等到生产者赚钱
            total_money-=money
            print(threading.current_thread().getName(),'----花了{}钱，当前余额为:{}'.format(money,total_money))
            lock.release()
def start():
    for i in range(5):
        prod=Producer(name='生产者{}'.format(i))
        prod.start()
    for i in range(5):
        cust=Customer(name='------消费者{}'.format(i))
        cust.start()


if __name__ == '__main__':
    start()
