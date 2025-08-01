import unittest
from unittest import mock,TestCase
from Package import call_app_func1
from Package import call_app_func2


class TestApi(TestCase):

    #
    def test_external_api(self):
        self.assertEqual(call_app_func1.func_call(),'hello person')
        self.assertEqual(call_app_func2.func_call2(), 'hello person')


    @mock.patch('Package.call_app_func2.app', return_value='Hello Monty')
    @mock.patch('Package.call_app_func1.app', return_value='Hello Simonto')
    def test_external_api_1(self,func_param,func_param2):
       # import pdb;pdb.set_trace()
        self.assertEqual(call_app_func1.func_call(),'Hello Simonto')
        self.assertEqual(call_app_func2.func_call2(), 'Hello Monty')


    def test_external_api_2(self):
        with mock.patch('Package.call_app_func2.app', return_value='Hello Monty'):
            self.assertEqual(call_app_func2.func_call2(), 'Hello Monty')


    @mock.patch('Package.call_app_func1.app', side_effect=['Hello Simonto',
                                                           'Hello Deep',
                                                           'Hello Roy'])
    def test_external_api_3(self,func_param):
       # import pdb;pdb.set_trace()
        self.assertEqual(call_app_func1.func_call(),'Hello Simonto')
        self.assertEqual(call_app_func1.func_call(), 'Hello Deep')
        self.assertEqual(call_app_func1.func_call(), 'Hello Roy')


    @mock.patch.object(call_app_func1,'app',return_value='Hello Vimdhayak')
    def test_external_api_4(self,func_param):
        self.assertEqual(call_app_func1.func_call(),'Hello Vimdhayak')



if __name__ == '__main__':
    unittest.main()

