import unittest
from unittest.mock import MagicMock,Mock
from myscript_24dec import *
from practice_for import Singleton,Callable,funcro,File
from unittest.mock import Mock,patch
from unittest.mock import MagicMock
def sum(x,y):
	return x.__add__(y)

def upper_words(x):
	return x.upper()


class Testall(unittest.TestCase):

	def testsum(self):
		self.assertEqual(sum(10,6),16)
	def test_upper_words_(self):
		self.assertEqual(upper_words('aradhna'),'ARADHNA')
	def test_foo(self):
		# import pdb;pdb.set_trace()
		self.assertEqual(foo('edi','zen','dev'),'123edizendev')
	def test_singleton(self):
		expected1=Singleton()
		expected2=Singleton()
		self.assertEqual(expected1,expected2)
	def test_funcro(self):
		self.assertEqual(funcro('Mandeep','Ranchi'),'Mandeepis from Ranchi')
		
	@patch('practice_for.File.__enter__')
	def test_file(self,mocked_file):
		ins=File('Myfile','wb+')
		mocked_file.return_value="You have entered FIle"
		self.assertEqual(ins.__enter__(),"You have entered FIle")
		
	def test_exit(self):
		mock_class_obj=File('Myfile','rb+')
		mock_class_obj.__exit__= MagicMock(return_value="Your out of file")
		self.assertEqual(mock_class_obj.__exit__(),"Your out of file")
		
	def test_called_once(self):
		mock=Mock()
		mock.upper_words('Binzap')
		mock.upper_words.assert_called_once()
		
	def test_called_once_with(self):
		mock=Mock()
		mock.sum(x='foo',y='baz')
		mock.sum.assert_called_once_with(x='foo',y='baz')
		self.assertEqual(sum(x='foo',y='baz'),'foobaz')
		
	def test_not_called_with(self):
		mock=Mock()
		
if __name__ == '__main__': 
    unittest.main() 
-----------------------------------
import unittest
import pytest
from unittest.mock import MagicMock,Mock
# from parameterized import parameterized, parameterized_class
from myscript_24dec import *
from practice_for import Singleton,Callable,funcro,File,A
from unittest.mock import Mock,patch
from unittest.mock import MagicMock
def sum(x,y):
	return x.__add__(y)

def upper_words(x):
	return x.upper()


class Testall(unittest.TestCase):

	def testsum(self):
		self.assertEqual(sum(10,6),16)
	def test_upper_words_(self):
		self.assertEqual(upper_words('aradhna'),'ARADHNA')
	def test_foo(self):
		# import pdb;pdb.set_trace()
		self.assertEqual(foo('edi','zen','dev'),'123edizendev')
	def test_singleton(self):
		expected1=Singleton()
		expected2=Singleton()
		self.assertEqual(expected1,expected2)
	
	def test_funcro(self):
		self.assertEqual(funcro('Mandeep','Ranchi'),'Mandeepis from Ranchi')
		
	@pytest.mark.parametrize("test_input,expected",[
	("Amandeep","Amandeep is from USA"),
	("Aman","Aman is from USA"),
	])	
	def test_A(test_input,expected):
		import pdb;pdb.set_trace()
		obj=A(input)
		self.assertEqual(obj.__str__(),expected)

		
	@patch('practice_for.File.__enter__')
	def test_file(self,mocked_file):
		ins=File('Myfile','wb+')
		mocked_file.return_value="You have entered FIle"
		self.assertEqual(ins.__enter__(),"You have entered FIle")
		
	def test_exit(self):
		mock_class_obj=File('Myfile','rb+')
		mock_class_obj.__exit__= MagicMock(return_value="Your out of file")
		self.assertEqual(mock_class_obj.__exit__(),"Your out of file")
		
	def test_called_once(self):
		mock=Mock()
		mock.upper_words('Binzap')
		mock.upper_words.assert_called_once()
		
	def test_called_once_with(self):
		mock=Mock()
		mock.sum(x='foo',y='baz')
		mock.sum.assert_called_once_with(x='foo',y='baz')
		self.assertEqual(sum(x='foo',y='baz'),'foobaz')
		
	def test_not_called_with(self):
		mock=Mock()
		
if __name__ == '__main__': 
    unittest.main() 