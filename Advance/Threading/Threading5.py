import time
import concurrent.futures

def do_something(secs):
    print(F"Sleep for {secs}\n")
    time.sleep(secs)
    return "Done sleeping"

t1 = time.perf_counter()

#Implement 10 thread to execute do_something method with specified number of second

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(do_something, 1) for _ in range(10)]

    #Look through all the future completed there execution to display result
    # Note: futures contins list of Future in order of complition of execution.
    for f in concurrent.futures.as_completed(futures):
        print(f.result())

t2 = time.perf_counter()
print(f"Scripts takes {round(t2-t1)} second (s)")
