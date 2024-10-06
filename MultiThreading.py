# run() − The run() method is the entry point for a thread.
# start() − The start() method starts a thread by calling the run method.
# join([time]) − The join() waits for threads to terminate.
# isAlive() − The isAlive() method checks whether a thread is still executing.
# getName() − The getName() method returns the name of a thread.
# setName() − The setName() method sets the name of a thread.

from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(0.3)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(0.3)

t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()

print("Bye")