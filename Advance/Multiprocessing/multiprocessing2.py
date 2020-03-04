import time
import multiprocessing
from multiprocessing import freeze_support

def do_something():
    print('Sleeping for 1 second')
    time.sleep(1)
    print('Done sleeping')


if __name__ == "__main__":
    freeze_support()

    start = time.perf_counter()
    p1 = multiprocessing.Process(target=do_something)
    p2 = multiprocessing.Process(target=do_something)

    p1.start()
    p2.start()

    #wait for p1 and p2 finish, Otherwise main script finish before P1 and P2 finishes it's excution.
    p1.join()
    p2.join()
    end = time.perf_counter()
    print(f'Script is finished in {round(end - start)} in second(s)')

