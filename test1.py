
def log(func):
    print('log')
    def gol(*v,**vv):
        print('gol')
        return func(*v,**vv)
    return gol

@log
def a(x):
    print('a',x)
    def b():
        print('b')
        return 
    return b()

a(4)
print('\n')
