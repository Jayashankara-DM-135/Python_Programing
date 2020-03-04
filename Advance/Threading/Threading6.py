import time
import concurrent.futures

def do_something(secs):
    print(F"Sleep for {secs}\n")
    time.sleep(secs)
    return f"Done sleeping {secs} second (s)"

t1 = time.perf_counter()

#Implement 5 threads to execute do_something method with second specified in list
secs = [1, 2, 3, 4, 5]
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Here submit() submit one function at a time.
    futures = [executor.submit(do_something, sec) for sec in secs]

    #Look through all the future completed there execution to display result
    for f in concurrent.futures.as_completed(futures):
        print(f.result())

t2 = time.perf_counter()
print(f"Scripts takes {round(t2-t1)} second (s)")
