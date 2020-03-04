import time
import concurrent.futures

def do_something(secs):
    print(F"Sleep for {secs}\n")
    time.sleep(secs)
    return f"Done sleeping {secs}"

t1 = time.perf_counter()

#Implement 5 thread to execute do_something method with specified number of second
secs = [5, 3, 4, 2, 1]
with concurrent.futures.ThreadPoolExecutor() as executor:
    # map() will create thread with function do_something for each value in 'secs'
    # returns results. But not futures.
    # Note: Results are stored in order in which thread started, But not order of complition.
    results = executor.map(do_something, secs)

    #if there any exception in function ,then it will raise when it's executing in thread
    # instead when values are retrived from iterator here "results".
    for res in results:
        #TODO: Handle anyexception while retriving value
        print(res)

t2 = time.perf_counter()
print(f"Scripts takes {round(t2-t1)} second (s)")
