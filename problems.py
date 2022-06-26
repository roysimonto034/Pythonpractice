from import_pract import Base
def show(x):
	Base.child(x)
show("bablu")

ar=[10,20,20,10,10,30,50,10,20]
ar=[15,12,15,10,15,30,50,15,12,15,10,12,10,15,10,10,15]
def pairs(np):
	par,flp=0,{}
	for i in np:
		flp[i]=np.count(i)
	for i in flp:
		if flp[i]>1:
			par+=(flp[i])//2
	return par
print(pairs(ar))

-----------------------socks pair problem-----------------------------

ar=[15,12,15,10,15,30,50,15,12,15,10,12,10,15,10,10,15]
def pairs(np,ar):
	par,flp=0,{}
	for i in range(np):
		flp[ar[i]]=ar.count(ar[i])
	for i in flp:
		if flp[i]>1:
			par+=(flp[i])//2
	return par
print(pairs(17,ar))


------------------------------------------------------------------------
import os
path=os.path.join('E:/','automate','testing')
print(path)
with open(os.path.join(path,"test_result.txt"),'r') as f:
	for i in f.readlines():
		import pdb;pdb.set_trace()
		print(i)
		
def func():
	import pdb;pdb.set_trace()
	try: 
		print("helllo")
		return 1
	finally:
		return 2
		
func()

def f(x):
	import pdb;pdb.set_trace()
	def f1(a, b):
		print("hello")
		if b==0:
			print("NO")
			return
		return f(a, b)
	return f1
@f
def f(a, b):
    return a%b
f(4,0)

from collections import deque
dlf=['def test1','import myname','myfunc(name)','return result','def nontest','func()','return result','def test2','calldeff','return reul','def test3','import myname','myfunc(name)','return result','def denontest',]
tx=[dlf.index(x) for x in dlf if x.startswith('def')]
gc,gt,fg=deque([0]),[],[]
dp=deque(tx)
dp.popleft()
for ip in range(len(tx)-1):
	gc.append(dp.popleft())
	if len(gc)==2:
		for i in range(gc[0],gc[1]):
			gt.append(dlf[i])
		fg.append(gt)
		gc.popleft()
		gt=[]
for kl in fg:
	import pdb;pdb.set_trace()
	if kl[0][4:8]!='test':
		fg.remove(kl)
print(fg)

import os		
class File(object):

	import pdb;pdb.set_trace()
	def __init__(self,fname,meth):
		self.fobj=open(fname,meth)
		
	def __enter__(self):
		return self.fobj
		
	def __exit__(self,type,vl,trace):
		self.fobj.close()
		
with File(os.path.join('D:\python_onhands','practice.txt'),'r') as fp:
	print(fp.read())
	
import argparse
import pdb;pdb.set_trace()
parser = argparse.ArgumentParser()
parser.add_argument("blog")
args = parser.parse_args()

if args.blog == 'deepu':
    print('You made it!')
else:
    print("Didn't make it!")

"""singleton implementation using __new__
Python"""
class Singleton(object):
    _instance = None  # Keep instance reference 
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance
		
class Callable(object):
	
	def __init__(self,func):
		self.func=func
	def __call__(self,*args,**kwargs):
		print("__call__ will be called first")
		return self.func(*args)
		

@Callable	
def funcro(a,b):
	return a+'is from '+b
	
# print(funcro('mandeep','ranchi'))

class A:
	def __init__(self,a):
		self.a=a
	def __call__(self,a):
		self.a=a
		return self.a +" is from United nations"
	def __str__(self):
		return self.a +" is from United nations"
a=A("manpreet")
print(a("Aman"))
	
# class Singleton(object):
    # _instance = None  # Keep instance reference 
    
    # def __new__(cls, *args, **kwargs):
        # if not cls._instance:
            # cls._instance = object.__new__(cls, *args, **kwargs)
        # return cls._instance
	
def outer_decorator(*outer_args,**outer_kwargs):                            
	# import pdb;pdb.set_trace()
	def decorator(fn):                                            
		def decorated(*args,**kwargs):                            
			for i in outer_args:
				print(i,end='')
			return fn(*args,**kwargs)                         
		return decorated                                          
	return decorator       
    
@outer_decorator(1,2,3)
def foo(a,b,c):
	print(a,end='')
	print(b,end='')
	print(c)
	
# foo('edi','zen','dev')



class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        self.file_obj.close()