import threading
# 创建一个锁对象
lock = threading.Lock()
def func():
    # 获取锁
    lock.acquire()
    try:
        # 临界区代码，只有获得锁的线程可以执行此代码块
        print("Critical section is running.")
    finally:
        # 释放锁
        lock.release()
# 创建线程
thread1 = threading.Thread(target=func)
thread2 = threading.Thread(target=func)
# 启动线程
thread1.start()
thread2.start()
# 等待线程完成
thread1.join()
thread2.join()
# 互斥锁（Mutex）：一种保护共享资源的锁，任何时候只允许一个线程持有互斥锁，从而访问共享资源。
# 临界区（Critical Sections）：通过使用互斥锁来保护的代码块，确保同一时间只有一个线程执行该代码块。
# 自旋锁（Spinlocks）：当锁不可用时，线程持续检查锁的状态，而不是在被阻塞的情况下休眠。
# 常用的同步机制包括：
# 锁（Locks）：防止多个线程同时执行临界区的代码。
# 信号量（Semaphores）：允许多个线程在一定数量的资源上进行竞争。
# 条件变量（Condition Variables）：允许线程在特定条件发生时才继续执行。
# 栅栏（Barriers）：使一组线程在所有线程都到达某个点之前都不会继续执行。

int s

wait( s )

{ while s <= 0 do no-op

s = s-1;

}

signal( s )

{s = s + 1;

}

for i in range(n):
    for j in range(m):
        d[i + j] += num[i][j]