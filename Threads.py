import time
from threading import Thread

def demo():
    print("Hello")
    time.sleep(2)
    print("Done")

if __name__=="__main__":
    #demo()
    #demo()
    t1=Thread(target=demo)
    t2=Thread(target=demo)
    t1.start()
    t2.start()

    t1.join()#wait till I finish
    t2.join()#wait till I finish

    print("Completed")

