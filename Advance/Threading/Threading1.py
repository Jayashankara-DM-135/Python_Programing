import time

def do_something():
    print("Sleeep for 1sec")
    time.sleep(1)
    print("Done !")

t1 = time.perf_counter()
do_something()
do_something()
t2 = time.perf_counter()
print(f"Scripts completes {t2-t1} second(s)")



