import logging

def outer(func):
    logging.basicConfig(filename="closer_logging.txt", level=logging.INFO)
    def inner(*args):
        logging.info("Method \"{}\" is called with args {}".format(func.__name__, args))
        print(func(*args))
    return inner

def add(*args):
    res = 0
    for arg in args:
        print(arg)
        res += int(arg)

def sub(a, b):
    return a-b

if "__name__ == __main__":
    add_inner = outer(add)
    sub_inner = outer(sub)

    args = (1, 2, 3, 4)
    print(add_inner(1, 2, 3, 4))

    sub_inner(5, 3)
