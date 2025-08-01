import unittest
from Employee import *
from unittest.mock import patch

class Test_method(unittest.TestCase):

    def setUp(self) -> None:
        # print("setUp")
        self.emp1=Employee("Monty","paneshwar",400000)
        self.emp2=Employee("Tim","Breshnan",500000)

    def tearDown(self) -> None:
        pass

    def test_unitest_method(self):
        #import pdb;pdb.set_trace()
        df= "Sum of all possible subarrays of the array"
        result=self.emp1.capital_kwords(df,3)
        self.assertEqual("SuM of alL poSsible suBarrays of thE arRay ",result)

    def test_unitest_method_2dncase(self):
        #import pdb;pdb.set_trace()
        df= "Sum of all possible subarrays of the array"
        result=self.emp1.capital_kwords(df,3)
        with self.assertRaises(AssertionError):
            self.assertEqual(result,"SuM of alL poSsible suBarrays of thE arRay")

    def test_employee_fullname(self):
        self.assertEqual(self.emp1.full_name,"Employee name is Monty paneshwar")
        self.assertEqual(self.emp2.full_name, "Employee name is Tim Breshnan")

    def test_employee_email(self):
        self.assertEqual(self.emp1.email, "Employee's mail id is paneshwar.Monty@monty.com")
        self.assertEqual(self.emp2.email, "Employee's mail id is Breshnan.Tim@monty.com")

    def test_salary(self):
        #import pdb;pdb.set_trace()
        self.emp1.payraise
        self.emp2.payraise
        self.assertEqual(self.emp1.pay,1000000.0)
        self.assertEqual(self.emp2.pay, 1250000.0)

    def test_url(self):
        #import pdb;pdb.set_trace()
        result=self.emp1.check_url()
        self.assertEqual(200,result[1])

    def test_mock(self):
        with patch('Employee.requests.get') as mock_obj:
            #import pdb;pdb.set_trace()
            mock_obj.return_value.ok=True
            mock_obj.return_value.status_code=200
            mock_obj.return_value.text='success'
            response=self.emp1.check_url()
            mock_obj.assert_called_with(self.emp1.url)
            self.assertEqual(response[0],"success")
            self.assertEqual(response[1],200)





if __name__ == '__main__':
    unittest.main()