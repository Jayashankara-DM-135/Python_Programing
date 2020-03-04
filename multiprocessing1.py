import time

start = time.perf_counter()

def do_something():
    print('Sleeping for 1 second')
    time.sleep(1)
    print('Done sleeping')

do_something()
do_something()

end = time.perf_counter()

print(f"Script is finished in {round(end-start)} second (s)")
