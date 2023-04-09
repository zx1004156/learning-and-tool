
def plus(*nums):
    res = 0
    for i in nums:
        res += i
    return res

print(plus(1,2,3,4,5,6,7,8,9))

------------------------
dt = {'sep': ' # ', 'end': '\n\n'}
print('hello', 'world', **dt)
 等同於 print('hello', 'world', sep=' # ', end='\n\n')
------------------------
def test(*args):
    print(args)

test(1,22,33,444)

def test(*args):
    for a in args:
        print("Optional argument: {}".format(a))
test(1,22,33,444)
------------------------
def test(**kwargs):
    print(kwargs)S

test(k = 1,g = 2, l = 3)

def test(**kwargs):
    for k,v in kwargs.items():
        print("Optional argument: key: {} value:{}".format(k,v))

test(k = 1,g = 2, l = 3)
------------------------
def printHello(func):
    def wrapper():
        print('Hello')
        return func()
    return wrapper

@printHello
def printWorld():
    print('World')

printWorld()
------------------------
@printHello 就是把printWorld() 帶入 printHello函數裡面
所以等於 printWorld() = printHello(printWorld())
