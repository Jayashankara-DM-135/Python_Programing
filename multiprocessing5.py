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
        futures = [executor.submit(do_something, i) for i in range(5)]

        for f in concurrent.futures.as_completed(futures):
            print(f.result())


    end = time.perf_counter()
    print(f'script is completed in {round(end-start)} seconds')
