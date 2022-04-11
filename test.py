import unittest

def add(a,b):
    result= a+b
    return result

class test (unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(5,10),15)
        
        
        
if __name__=="__main__":
    unittest.main()