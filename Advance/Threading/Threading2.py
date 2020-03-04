import time
import threading

def do_something(secs):
    print(f"Sleep for {secs} sec\n")
    time.sleep(secs)
    print("Done \n")

t1 = time.perf_counter()
thread1 = threading.Thread(target=do_something, args=[1])
thread2 = threading.Thread(target=do_something, args=[2])
thread1.start()
thread2.start()


thread1.join()
thread2.join()

t2 = time.perf_counter()

print(f'Script takes {round(t2-t1)} second(s)')
