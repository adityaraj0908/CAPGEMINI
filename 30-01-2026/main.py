import pytest
import unittest
from abc import ABC, abstractmethod




# def func(x):
#     return x+5

# def test_method():
#     assert func(3)==5







# def find_square(x):
#     return x**2

# def test_method():
#     assert find_square(4)==16
    



# def even_odd(n):
#     if n%2==0:
#         return "even"
#     return "odd"

# def test_method_even():
#     assert even_odd(4)=="even"

# def test_method_odd():
#     assert even_odd(5)=="odd"
    







# def prime_number(n):
#     count = 0
#     for i in range(1,(n//2)+1):
#         if n%i==0:
#             count+=1
    
#     if count ==1:
#         return "prime"
#     return "non-prime"


# def test_prime_true():
#     assert prime_number(3) == "prime"

# def test_prime_false():
#     assert prime_number(6) == "non-prime"







# def test_answer1():
#     a = 5
#     b = 10
#     assert a==b

# def test_answer2():
#     c = 15
#     d = 15
#     assert c ==d

# def test_answer3():
#     assert 4%2 ==0










# def to_upper(s):
#     return s.upper()

# def get_length(s):
#     return len(s)

# def test_upper():
#     assert to_upper("pytest") == "PYTEST"

# def test_length():
#     assert get_length("python") == 6



# def total(lst):
#     return sum(lst)

# def maximum(lst):
#     return max(lst)

# def test_total():
#     assert total([1,2,3]) == 6

# def test_maximum():
#     assert maximum([4,5,6]) == 6








# def div(a,b):
#     return a/b

# def test_div_zero():
#     with pytest.raises(ZeroDivisionError):
#         div(5,0)






# class BankAccount:
#     def __init__(self, initial_balance=0):
#         self.__balance = initial_balance  

#     def deposit(self, amount):
#         if amount <= 0:
#             raise ValueError("Deposit amount must be positive")
#         self.__balance += amount

#     def withdraw(self, amount):
#         if amount <= 0:
#             raise ValueError("Withdraw amount must be positive")
#         if amount > self.__balance:
#             raise ValueError("Insufficient balance")
#         self.__balance -= amount

#     def get_balance(self):
#         return self.__balance



# def test_initial_balance():
#     acc = BankAccount(100)
#     assert acc.get_balance() == 100

# def test_deposit():
#     acc = BankAccount(100)
#     acc.deposit(50)
#     assert acc.get_balance() == 150

# def test_withdraw():
#     acc = BankAccount(200)
#     acc.withdraw(50)
#     assert acc.get_balance() == 150

# def test_balance_cannot_be_modified_directly():
#     acc = BankAccount(100)
#     acc.__balance = 10000  
#     assert acc.get_balance() == 100   
    
# def test_withdraw_more_than_balance():
#     acc = BankAccount(100)
#     with pytest.raises(ValueError):
#         acc.withdraw(200)

# def test_invalid_deposit():
#     acc = BankAccount()
#     with pytest.raises(ValueError):
#         acc.deposit(-10)















# from abc import ABC, abstractmethod

# class Vehicle(ABC):

#     @abstractmethod
#     def start(self):
#         pass


# class Bike(Vehicle):
#     def start(self):
#         return "Bike engine started"
    
# class Car(Vehicle):
#     def start(self):
#         return "Car engine started"
    
# class Truck(Vehicle):
#     pass

# car = Car()
# bike = Bike()

# print(car.start())
# print(bike.start())


# def test_car_start():
#     car = Car()
#     assert car.start() == "Car engine started"


# def test_vehicle_cannot_be_instantiated():
#     with pytest.raises(TypeError):
#         Vehicle()


# def test_bike_start():
#     bike = Bike()
#     assert bike.start() == "Bike engine started"


# def test_truck_without_start_method():
#     with pytest.raises(TypeError):
#         Truck()










# class Shape(ABC):

#     @abstractmethod
#     def area(self):
#         pass

# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return 0.5 * self.base * self.height
    
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius
    
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width


# class TestShapeArea(unittest.TestCase):

#     def test_rectangle_area(self):
#         rect = Rectangle(10, 5)
#         self.assertEqual(rect.area(), 50)

#     def test_circle_area(self):
#         circle = Circle(7)
#         self.assertAlmostEqual(circle.area(), 153.86, places=2)
   
#     def test_triangle_area(self):
#         tri = Triangle(10, 4)
#         self.assertEqual(tri.area(), 20)
    
#     def test_shape_is_abstract(self):
#         with self.assertRaises(TypeError):
#             Shape()
   
   
# if __name__ == "__main__":
#     unittest.main()















# class Student:
#     def __init__(self, name, roll_no):
#         self.name = name
#         self.roll_no = roll_no


# class TestStudent(unittest.TestCase):

#     def test_student_initialization(self):
#         s = Student("Aditya", 101)
#         self.assertEqual(s.name, "Rahul")
#         self.assertEqual(s.roll_no, 101)

# if __name__ == "__main__":
#     unittest.main()

















# class Bank(ABC):

#     @abstractmethod
#     def getInterestRate(self):
#         pass

# class SBI(Bank):
#     def getInterestRate(self):
#         return 6.5

# class HDFC(Bank):
#     def getInterestRate(self):
#         return 7.0

# class TestBankInterestRates(unittest.TestCase):

#     def test_sbi_interest_rate(self):
#         sbi = SBI()
#         self.assertEqual(sbi.getInterestRate(), 6.5)

#     def test_hdfc_interest_rate(self):
#         hdfc = HDFC()
#         self.assertEqual(hdfc.getInterestRate(), 7.0)

#     def test_bank_is_abstract(self):
#         with self.assertRaises(TypeError):
#             Bank()


# if __name__ == "__main__":
#     unittest.main()
















# SINGLE INHERTITANCE

# class Animal:
#     def speak(self):
#         return "Animal sound"

# class Dog(Animal):
#     def speak_again(self):
#         return "Bark"
    


# class TestSingleInheritance(unittest.TestCase):
#     def test_dog_speak(self):
#         d = Dog()
#         self.assertEqual(d.speak(), "Animal sound")







#MULTI-LEVEL INHERITANCE

# class Vehicle:
#     def type(self):
#         return "Vehicle"

# class Car(Vehicle):
#     def wheels(self):
#         return 4

# class ElectricCar(Car):
#     def fuel(self):
#         return "Electric"
    
# class TestMultilevelInheritance(unittest.TestCase):
#     def test_electric_car(self):
#         ev = ElectricCar()
#         self.assertEqual(ev.wheels(), 4)
#         self.assertEqual(ev.fuel(), "Electric")
#         self.assertEqual(ev.type(), "Vehicle")
















#MULTIPLE INHERITANCE

# class Engine:
#     def engine_type(self):
#         return "Petrol"

# class MusicSystem:
#     def engine_type(self):
#         return "Diesel"
    
#     def music(self):
#         return "Music On"

# class Car(Engine, MusicSystem):
#     pass


# class TestMultipleInheritance(unittest.TestCase):
#     def test_car_features(self):
#         c = Car()
#         self.assertEqual(c.engine_type(), "Petrol")
#         self.assertEqual(c.music(), "Music On")




# if __name__ == "__main__":
#     unittest.main()













def process_matrix(n, matrix):
   
    for i in range(n):
        matrix[i] = matrix[i][::-1]

    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0

    return matrix




# class TestMatrix(unittest.TestCase):

#     def test_basic_matrix(self):
#         n = 3
#         matrix = [
#             [1, 0, 0],
#             [0, 1, 0],
#             [1, 1, 1]
#         ]

#         expected = [
#             [1, 1, 0],
#             [1, 0, 1],
#             [0, 0, 0]
#         ]

#         self.assertEqual(process_matrix(n, matrix), expected)


# if __name__ == "__main__":
#     unittest.main()








def test_basic_matrix():
    n = 3
    matrix = [
        [1, 0, 0],
        [0, 1, 0],
        [1, 1, 1]
    ]

    expected = [
        [1, 1, 0],
        [1, 0, 1],
        [0, 0, 0]
    ]

    assert process_matrix(n, matrix) == expected


