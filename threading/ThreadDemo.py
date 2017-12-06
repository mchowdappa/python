
from threading import Thread
class MyMessanger(threading.Thread):

     def run(self):
         for _ in range(100):
             print(threading.currentThread().getName())


t1 = MyMessanger(name="T1")
t2 = MyMessanger(name="T2")
t1.start()
t2.start()
