import unittest


# def square(n):
#   return n*n

# class TestSquare(unittest.TestCase):
#   def test_square(self):
#     self.assertEqual(square(4), 16)

# unittest.main()





















# class TestDemo(unittest.TestCase):
#   def setUp(self):
#     self.a=10
#     self.b=5

#   def test_add(self):
#     self.assertEqual(self.a+self.b, 15)

#   def tearDown(self):
#     pass

# def withdraw(balance,amount):
#   if amount>balance:
#     raise ValueError("Insufficient Funds")
#   return balance-amount

# def test_exception(self):
#   with self.assertRaises(ValueError):
#     withdraw(100,200)

# class Bank:
#   def deposit(self,amt):
#     return amt

# class TestBank(unittest.TestCase):
#   def test_deposit(self):
#     bank=Bank()
#     self.assertEqual(bank.deposit(1000),1000)

# @unittest.skip("feature not ready")
# def test_future(self):
#   pass






















# class TestStringMethods(unittest.TestCase):
#     def setUp(self):
#         pass

#     def test_strings_a(self):
#         self.assertEqual('a'*4,'aaaa')
    
#     def test_upper(self):
#         self.assertEqual('foo'.upper(),'FOO')

#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper()) 
    
#     def test_strip(self):
#         s='jayamamam'
#         self.assertEqual(s.strip('jaya'),'jayanam')

#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(),['hello','world'])
#         with self.assertRaises(TypeError):
#             s.split(2)
        
# if __name__ == '__main__':
#     unittest.main()








# class Widget:
#     def __init__(self,name):
#         self.name = name

#     def size(self):
#         return (50,50)

# class DefaultWidgetSizeTestCase(unittest.TestCase):
#     def test_default_widget(self):
#         widget = Widget("The Widget")
#         self.assertEqual(widget.size(),(50,50))

    

# class WidgetTestCase(unittest.TestCase):
#     def setUp(self):
#         self.widget = Widget("The Widget")

#     def tearDown(self):
#         self.widget.dispose()

# if __name__ == '__main__':
#     unittest.main()












# import unittest

# class WidgetTestCase(unittest.TestCase):
#     def test_default_widget_size(self):
#         self.assertEqual(1, 1)

#     def test_widget_resize(self):
#         self.assertTrue(True)


# def suite():
#     suite = unittest.TestSuite()
#     suite.addTest(WidgetTestCase('test_default_widget_size'))
#     suite.addTest(WidgetTestCase('test_widget_resize'))
#     return suite


# if __name__ == '__main__':
#     runner = unittest.TextTestRunner()
#     runner.run(suite())
















# def tower_of_hanoi(n, src, aux, dest):

#     if n == 1:
#         print(f"Move disk 1 from {src} to {dest}")
#         return

#     tower_of_hanoi(n-1, src, dest, aux)

#     print(f"Move disk {n} from {src} to {dest}")

#     tower_of_hanoi(n-1, aux, src, dest)


# n = int(input("Enter number of disks: "))
# tower_of_hanoi(n, "A", "B", "C")










# class Widget:
#     def __init__(self):
#         self.width = 50
#         self.height = 50

#     def resize(self,width,height):
#         self.width = width
#         self.height = height

    


# class WidgetTestCase(unittest.TestCase):

#     def test_default_widget_size(self):
#         widget = Widget()
#         self.assertEqual(widget.width,50)
#         self.assertEqual(widget.height,50)


#     def test_widget_resize(self):
#         widget = Widget()
#         widget.resize(100,150)
#         self.assertEqual(widget.width,100)
#         self.assertEqual(widget.height,150)
        

# if __name__ == '__main__':
#     unittest.main()



# class MyTestCase(unittest.TestCase):

#     @unittest.skip("demonstrating skipping")
#     def test_nothing(self):
#         self.fail("shouldn't happen")

#     @unittest.skipIf(mylib.__version__<(1,3),"not supported in this library version")
#     def test_format(self):
#         pass

#     @unittest.skipUnless(sys.platform.startswith("win"),"requires Windows")
#     def test_windows_support(self):
#         pass

#     def test_maybe_skipped(self):
#         if not external_resource_available():
#             self.skipTest("External resource not available")
#         pass

# @unittest.skip("Showing class Skipping")
# class MySkippedTestCase(unittest.TestCase):
#     def test_not_run(self):
#         pass

# class ExpectedFailureTestCase(unittest.TestCase):
#     @unittest.expectedFailure
#     def test_fail(self):
#         self.assertEqual(1,0,"broken")


# def skipUnlessHasattr(obj,attr):
#     if hasattr(obj,attr):
#         return lambda func: func
    
#     return unittest.skip("{!r} doesn't have {!r}".format(obj,attr))












# class NumbersTest(unittest.TestCase):
#     def test_even(self):
#         for i in range(0,6):
#             with self.subTest(i=i):
#                 self.assertEqual(i%2,0)

# if __name__ == "__main__":
#     unittest.main()








# import unittest

# def square(n):
#     return n*n

# class TestSquare(unittest.TestCase):
#     def test_square_values(self):
#         test_data = [
#             (2,4),(3,9),(4,16),(5,25)
#         ]
        
#         for num, expected in test_data:
#             with self.subTest(num=num):
#                 self.assertEqual(square(num), expected)
                
# if __name__ == '__main__':
#   unittest.main()











# import unittest

# class TestStringLength(unittest.TestCase):
#     def test_string_length(self):
#         strings = {
#             "apple": 5, 
#             "banana": 6,
#             "cat": 3,
#             "Aditya":5
#         }
        
#         for text, length in strings.items():
#             with self.subTest(string = text):
#                 self.assertEqual(len(text), length)

# if __name__ == '__main__':
#     unittest.main()










# import unittest

# def square(n):
#     return n*n

# class TestSquare(unittest.TestCase):
#     def test_float_square_values(self):
#         test_data = [
#             (0.2,0.04)
#         ]
        
#         for num, expected in test_data:
#             with self.subTest(num=num):
#                 self.assertEqual(square(num), expected)
        
                
# if __name__ == '__main__':
#   unittest.main()








# def is_valid_password(pwd):
#     return len(pwd)>8

# class TestPassword(unittest.TestCase):

#     def test_password(self):
#         password = [
#             ("password123",True),
#             ("abc",False),
#             ("welcome12",True),
#             ("123456",False)     
#         ]

#         for pwd,expected in password:
#             with self.subTest(password=pwd):
#                 self.assertEqual(is_valid_password(pwd),expected)


# if __name__ == "__main__":
#     unittest.main()





# import unittest

# def divide(a, b):
#     if b == 0:
#         raise ValueError("Division by zero")
#     return a / b

# class TestDivide(unittest.TestCase):

#     def test_division(self):
#         test_cases = [
#             (10, 2, 5),
#             (20, 4, 5)
#         ]
#         for a, b, result in test_cases:
#             with self.subTest(a=a, b=b):    
#                 self.assertEqual(divide(a, b), result)

#     def test_divide_by_zero(self):
#         for b in [0]:
#             with self.subTest(b=b):
#                 self.assertRaises(ValueError, divide, 10, b)

# if __name__== "__main__":
#     unittest.main()














# import unittest

# def add(a, b):
#     return a + b

# class TestAddFunction(unittest.TestCase):
#     def test_add_positive_numbers(self):
#         self.assertEqual(add(1, 2), 3)

#     def test_add_negative_numbers(self):
#         self.assertEqual(add(-1,-2), -3)

#     def test_add_mixed_numbers(self):
#         self.assertEqual(add(1, -2), -1)
#         self.assertEqual(add(-1, 2), 1)

# if __name__== '__main__':
#     unittest.main()


# import unittest
# def add(a, b): 
#     return a + b

# class TestAdd(unittest.TestCase):
#     def test_positive(self):
#         self.assertEqual(add(2, 3), 5)
#     def test_negative(self):
#         self.assertEqual(add (-2, -3), -5)
#     def test_mixed (self):
#         self.assertEqual(add(5, -2), 3)


# if __name__ == "__main__":
#     unittest.main()









import unittest
def is_even(number):
    return number % 2 == 0

class TestEvenOdd(unittest. TestCase):
    def test_even_number(self): 
        self.assertTrue(is_even(4))
    def test_odd_number(self): 
        self.assertFalse(is_even(7))
    def test_zero(self):
        self.assertTrue(is_even(0))

if __name__ == "__main__":
    unittest.main()