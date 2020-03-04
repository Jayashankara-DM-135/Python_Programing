def mylogging(func):
    import logging
    logging.basicConfig(filename="{}.log".format(func.__name__), level=logging.INFO)
    def wrapper(*args, **kwargs):
        logging.info("{} method called with {} and {} args".format(*args, **kwargs))
        return func()
    return wrapper

@mylogging
def test():
    print("Tets method is called")

@mylogging
def verfiy(arg1=10, arg2=20):
    print("Verfiy method is called")

test()
verify()
verify(40,50)

