import unittest


class Test(unittest.TestCase):
    
    # Returns True if the string contains 4 '1'.
    def test_string(self):
        self.assertEqual( '1'*4, '1111')
        ##self.assertEqual( '1'*4, '111')



class Test1(unittest.TestCase):
    
    # Returns True if the string is in upper case.
    def test_upper(self):
        self.assertEqual('hopper'.upper(), 'HOPPER')
        ##self.assertEqual('Hopper'.upper(),'hopper')


class Test2(unittest.TestCase):
      # Returns True if the string is in lower case.
      def test_lower(self):
        self.assertEqual('ALIO'.lower(), 'alio')
        ##self.assertEqual('ten'.lower(),'TEN')



class Test3(unittest.TestCase):
    # Returns True if the Square of Number 4 is 16
    def test_square(self):
        self.assertEqual(4*4,16)
        ##self.assertEqual(4*4,24)



class Test4(unittest.TestCase):
    
    # Returns true if the string splits and matches
    # the given output.
    def test_split(self):        
        s = 'Quality Assurance'
        self.assertEqual(s.split(), ['Quality', 'Assurance'])
        ##self.assertEqual(s.split(), ['Quality', 'Measure'])
        with self.assertRaises(TypeError):
            s.split(2)



class Test5(unittest.TestCase):
    # Return True if Greatest Common Divisor of 5 and 10 is 5
    def test_gcd(self):
       self.assertEqual(5%10,5)
       ##self.assertEqual(5%10,4)        



if __name__=='__main__':
    unittest.main()

suite = unittest.TestSuite()
suite.addTests([Test( 'test_string'),Test1('test_upper'),Test2('test_lower'),Test3('test_square'),Test4('test_split'),Test5('test_gcd')])
runner = unittest.TextTestRunner(verbosity=6)
result = runner.run(suite)
