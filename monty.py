'''This is to demonstrate factory pattern class''' 

class A:

    def method(self):
        return "hello A"
class B:

    def method(self):
        return "hello B"


def factory(obj=None):
    dctobj = {'a':A(),'b':B()}
    return dctobj[obj]

ef=factory('a')
print(ef.method())
eg=factory('b')
print(eg.method())


class Myexception(Exception):

    def __init__(self,message):
        super(Myexception, self).__init__(message)

message="junk Exception raised"


def testexec(val):
    val['name'] = 'Monty'
    try:
        if val['age'] == 45:
            raise Myexception(message)
    except Exception as e:
        print(str(e))

testexec({'age':45})


class Jpmorgan:

    def lob(self):
        print("this Jp morgan Lob"+'EPIX')

    def location(self):
        print ("this is Jp morgan Mumbai")


class Stanc:

    def lob(self):
        print("this is Standard chartered Lob" + 'FXO')

    def location(self):
        print ("this is Stanc Chennai")


def polymorphism(obj):
    obj().lob()
    obj().location()


polymorphism(Jpmorgan)
polymorphism(Stanc)

import time


def decorated(*orgs, **kwargs):
    def decor(func):
        def inner_func(*args, **kwargs):
            #import pdb;pdb.set_trace()
            t1=time.time()
            time.sleep(5)
            result = func(*args, **kwargs)
            t2 = time.time()-t1
            print("function "+func.__name__+" took "+str(t2)+" seconds")
            return orgs[0]+str(args[0])+orgs[1]+str(args[1])+orgs[2]+str(result)
        return inner_func
    return decor

@decorated("Sum of "," and "," is: ")
def callfunc(a, b):
    sums = a+b
    return sums

print(callfunc(3,4))
#print(pf)
def outer_decorator(*outer_args, **outer_kwargs):
    # import pdb;pdb.set_trace()
    def decorator(fn):
        def decorated(*args, **kwargs):
            sn = ''
            for i in outer_args:
                sn += str(i)
            return sn + fn(*args, **kwargs)

        return decorated

    return decorator


@outer_decorator(1, 2, 3)
def foo(a, b, c):
    return (a + b + c)


pt = foo('edi', 'zen', 'dev')
print(pt)


class SquareDecorator:

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        # before function
        result = self.function(*args, **kwargs)

        # after function
        return result


# adding class decorator to the function
@SquareDecorator
def get_square(n):
    print("given number is:", n)
    return n * n


print("Square of number is:", get_square(195))


