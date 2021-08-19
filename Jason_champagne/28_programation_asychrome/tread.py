import time
import threading

my_lock = threading.RLock() #c'est la mise en place du verrou dans les thread

class Myprocess(threading.Thread):
    def __init(self):
        threading.Thread.__init__(self)

    def run(self):
        i = 0
        while i < 5:
            #print(threading.current_thread())#affiche le nom du thread en cours
            with my_lock:#ici c'est l'intégration du thread il est mis sur la suite  de l'opération ici letter, lee verou est mis sur les partie du traitrement qui peut causer problème ou critique
                letters = "ABCDEFGH"
                for it in letters:
                    print(it)
                    time.sleep(0.3)
            #time.sleep(0.3)
            i += 1

th1 = Myprocess()
th2 = Myprocess()

th1.start()
th2.start()

th1.join()
th2.join()