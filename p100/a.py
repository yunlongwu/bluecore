#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Queue,Process
import time

q = Queue()

def worker(name):
    i = 0
    while i<20:
        time.sleep(1)
        q.put(i)
        i += 1
        print("%s生产了%s个商品"%(name,i))

def consumer(name):
    j = 0
    while j<21:
        time.sleep(1)
        if not q.empty():
            q.get()
            j+=1
            print("%s消费了%s个商品"%(name,j))
        elif q.empty() and j==20:
            print("全部消费完")
            return
        else:
            print("B消费快了，等等生产")

if __name__ == '__main__':
    wo = Process(target=worker,args=('A'))
    co = Process(target=consumer,args='B')
    wo.start()
    co.start()






