import os
path=os.path.join('E:/backup_script.py')
with open(path,'r') as f:
	xc=[]
	import pdb;pdb.set_trace()
	for ip in f.readlines():
		if 'def' in ip:
			xc.append(ip)
	print(xc)
	for i in xc:
import pytest
	
def dethod(*args,**kwargs):
	for i in args:
		fp=2.5*i+4
		return fp
print(dethod(23,12,13))

def fdp(pj):
	import pdb;pdb.set_trace()
	return "PROTOTYPE "+str(pj)
	
def mymeth(func):
	def inner_func(para):
		func(para)
	return inner_func

tesp=mymeth(fdp)



@pytest.mark.parametrize("input,output",[(23,61.5),(12,34),(13,36.5)])
def test_dethod(input,output):
	import pdb;pdb.set_trace()
	assert dethod(input)==output
	
def test_mymeth(tesp):
	assert tesp('required')== "PROTOTYPE required"
	
	pytest --cov=/registration/al/WebAPI/webapiserver/setting/controllers/ --cov-reportt erm-missing /home/SYSROM_SRC/Pytest/UT/setting/controllers/  --cov-report=html
	
	
NO OSS related changes
A> NO
B> NA
C> NA


def outer_decorator(*outer_args,**outer_kwargs):                            
	# import pdb;pdb.set_trace()
	def decorator(fn):                                            
		def decorated(*args,**kwargs):  
			sn=''
			for i in outer_args:
				sn+=str(i)
			return sn+fn(*args,**kwargs)                         
		return decorated                                          
	return decorator       
    
@outer_decorator(1,2,3)
def foo(a,b,c):
	return(a+b+c)
	
pt=foo('edi','zen','dev')
print(pt)