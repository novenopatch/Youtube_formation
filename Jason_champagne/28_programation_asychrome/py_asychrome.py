import time 
import  threading

def process1 ():
    i = 0
    while i < 5:
        print("cou")
        time.sleep(0.3)
        i += 1
def process2 ():
    i = 0
    while i < 5:
        print("ccccccccca grrrrrrrrrr")
        time.sleep(0.3)
        i += 1

t1 = threading.Thread(target=process1)
t2 = threading.Thread(target=process2)

t1.start()
t2.start()

t1.join()
t2.join()