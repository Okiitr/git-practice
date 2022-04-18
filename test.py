import unittest

def add(a,b):
    result= a+b
    return result
def sub(a,b):
    result= a-b
    return result
def mul(a,b):
    result= a*b
    return result


class test (unittest.TestCase):
    
    def setUp(self) -> None:
        print('you are in setUp')
    def tearDown(self) -> None:
        print('you are in tearDown \n')
    
    def test_add(self):
        self.assertEqual(add(5,10),15)
    def test_sub(self):
        self.assertEqual(sub(15,10),5)
    def test_mul(self):
        self.assertEqual(mul(5,10),50)
        
        
        
if __name__=="__main__":
    unittest.main()