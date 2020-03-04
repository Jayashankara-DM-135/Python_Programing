import time
import threading

def do_something(secs):
    print(f'sleeps for {secs} second (s)\n')
    time.sleep(secs)
    print('Done\n')

threads = []

t1 = time.perf_counter()
for _ in range(10):
    thread = threading.Thread(target=do_something, args=[2])
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

t2 = time.perf_counter()
print(f'Scripts completes in {round(t2-t1)} second (s)')
