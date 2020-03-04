"""
3.5.2 processPoolExecutor ==> Swith between mutithredaing and muti-process is posible:
"""

import time
from multiprocessing import freeze_support
import concurrent.futures

def do_something(secs):
    print(f'Sleep for {secs} seconds')
    time.sleep(secs)
    return F'Done for sleeping {secs}'


if __name__ == '__main__':
    freeze_support()

    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        p1 = executor.submit(do_something, 1)
        p1 = executor.submit(do_something, 1)
        print(p1.result())

    end = time.perf_counter()
    print(f'script is completed in {round(end-start)} seconds')
