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
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something, secs)

        for res in results:
            #Handle execption here.
            print(res)

    end = time.perf_counter()
    print(f'script is completed in {round(end-start)} seconds')
