def printHello(func):
    def wrapper():
        print('Hello')
        return func()
    return wrapper

@printHello
def printWorld():
    print('World')

printWorld()