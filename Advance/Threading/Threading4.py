"""
context manager will have threadpoll which will provides effieient way of implementing thread.
It also helps to switch between mutiple process and threads.

supported by python 3.2 and above.

"""
import time
import concurrent.futures

def do_something(secs):
    print(F"sleep for {secs} second (s)")
    time.sleep(secs)
    return "Done sleeping"

t1 = time.perf_counter()
# context manger will wait for all Future object finish there execution.
# No need to explicity specify about join() here.
with concurrent.futures.ThreadPoolExecutor() as executor:
    # submit method schdule the thread and returs future object like f1 and f2 here.
    # future object encapulates methods to be executed and return value upon completion
    f1 = executor.submit(do_something, 1)
    f2 = executor.submit(do_something, 2)

    # This will wait till future object completes schdule thread
    print(f1.result())
    #We can skip checking the return for f2

t2 = time.perf_counter()

print(f'Scripts complete execution in {round(t2-t1)} second (s)')




