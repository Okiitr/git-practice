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
    
    def test_add(self):
        self.assertEqual(add(5,10),15)
    def test_sub(self):
        self.assertEqual(sub(15,10),5)
    def test_add(self):
        self.assertEqual(mul(5,10),50)
        
        
        
if __name__=="__main__":
    unittest.main()