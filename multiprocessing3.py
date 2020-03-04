import time
import multiprocessing
from multiprocessing import freeze_support

def do_something(sec):
    print(F"Sleep for {sec} ")
    time.sleep(sec)
    print(F"Done sleeping {sec}")

if __name__ == '__main__':
    start = time.perf_counter()

    process = [multiprocessing.Process(target=do_something, args=[i]) for i in range(5)]
    for p in process:
        p.start()

    for p in process:
        p.join()

    end = time.perf_counter()
    print(F"script completed in {round(end - start)} second (s)")
