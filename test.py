"""import threading
import os
print("bla")
start_new_thread
os.system("python test2.py")
print("b")
"""
def func1():
    os.system("handler.py")
def func2():
    while True:
        print("lalllla")
from multiprocessing import Process
import multiprocessing
p1 = Process(target=func1)
p1.start()
p2 = Process(target=func2)
p2.start()
p1.join()
p2.join()
