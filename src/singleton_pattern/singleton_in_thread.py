import threading

from singleton_with_new import Singleton

a = {"a": 1}


def init_singleton():
    s = Singleton()
    print(s)


if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=init_singleton)
    t2 = threading.Thread(target=init_singleton)

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

    # both threads completely executed
    print(a)
    print("Done!")
