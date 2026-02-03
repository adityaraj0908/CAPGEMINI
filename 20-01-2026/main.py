# name = "Aditya"

# rev = ""
# for ch in name:
#     rev = ch + rev

# print(rev)









# class Dog:
#     species = "Canine"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# d1 = Dog("ABC",12)
# d1 = Dog("XYZ",12)
# d1 = Dog("RAMHUL",12)
# d1 = Dog("RAHUL",12)
# d1 = Dog("ABC",12)

# print(d1.species)
# print(d1.name)
# print(d1.age)









# class Human:
#     species = "HomoSapien"

#     def __init__(self, name , age):
#         self.name = name
#         self.age = age

# name1 = Human("Aditya",22)
# name2 = Human("Rahul",8)
# name3 = Human("ABC",20)
# name4 = Human("XYZ",31)
# name5 = Human("Python",29)

# print(name2.species)













# class Data:
#     def __init__(self,name,age,phone,pan):
#         self.name = name
#         self.age = age
#         self.phone = phone
#         self.pan = pan


# name = input("Name: ")
# age = int(input("Age: "))
# phone = input("Phone: ")
# pan = input("PAN: ")

# obj = Data(name,age,phone,pan)
# print(obj.name)
# print(obj.age)
# print(obj.phone)
# print(obj.pan)


# name = input("Name: ")
# age = int(input("Age: "))
# phone = input("Phone: ")
# pan = input("PAN: ")

# obj1 = Data(name,age,phone,pan)
# print(obj1.name)
# print(obj1.age)
# print(obj1.phone)
# print(obj1.pan)













# class Bird:
#     def __init__(self, name):
#         self.name = name

#     def display_name(self):
#         print(f"Bird's Name: {self.name}")

# class Cuckoo(Bird):  
#     def sound(self):
#         print("Cuckoo sings")

# class HummingBird(Cuckoo):  
#     def sing(self):
#         print(f"{self.name}Sings !!")

# class Friendly:
#     def greet(self):
#         print("Friendly singing!")

# class Sparrow(Bird, Friendly):  
#     def sound(self):
#         print("Golden Retriever Barks")


# my_bird = Cuckoo("Tweeny")
# my_bird.display_name()
# my_bird.sound()

# other_bird = HummingBird("abc")
# other_bird.display_name()
# other_bird.sing()

# another_bird = Sparrow("Charlie")
# another_bird.display_name()
# another_bird.sound()
# another_bird.greet()







# def prime_number(n):
#     count =0
#     for i in range(1,n):
#         if n%i==0:
#             count+=1
#     if count ==1:
#         return True
#     return False

# print(prime_number(15))





# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fib(n-1) + fib(n-2)

# n = int(input("Enter number of terms: "))
# for i in range(n):
#     print(fib(i), end=" ")






# class Calculator:
#     def multiply(self,a=1,b=1,*args):
#         result = a*b
#         for num in args:
#             result*=num
#         return result


# calc = Calculator()


# print(calc.multiply())
# print(calc.multiply(4))
# print(calc.multiply(3,4))
# print(calc.multiply(3,4,6,7,8,9))






# class Animal:
#     def sound(self):
#         return "Some generic sound"
    
# class Dog(Animal):
#     def sound(self):
#         return "bark"

# class Cat(Animal):
#     def sound(self):
#         return "Meow"
    
# animals = [Cat(),Dog(),Animal()]

# for animal in animals:
#     print(animal.sound())








# class Goa:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def go_to_beach(self):
#         return "Enjoying on beach"

#     def go_to_temple(self):
#         return "Worshiping"
    
#     def go_to_club(self):
#         return "Partying"
    
#     def go_to_restaurant(self):
#         return "Eating Meal"
    
#     def play_music(self):
#         return "Playing instrument"
    


# person1 = Goa()








# class Pen:
#     def use(self):
#         return "Writing"
    
# class Eraser:
#     def use(self):
#         return "Erasing"

# def perform_task(tool):
#     print(tool.use())

# perform_task(Pen())
# perform_task(Eraser())







# class Example:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age




    
# ex = Example("Aditya",20)
# print(ex.name)
# print(ex.newvar)




# class BankAccount:
#     def __init__(self,n):
#         self.balance = n
    
#     def _show_balance(self):
#         print(self.balance)
        
#     def __update_balance(self, amount):
#         self.balance += amount
        
#     def deposit(self, amount):
#         if amount > 0:
#             self.__update_balance(amount)
#             self._show_balance()
#         else:
#             print("Invalid")

# account = BankAccount(1000)
# account._show_balance()
# account.deposit(1000)




# class Employee:
#     def __init__(self):
#         self.__salary = 50000
    
#     def get_salary(self):
#         return self.__salary

#     def set_salary(self,amount):
#         if amount>0:
#             self.__salary = amount
#         else:
#             print("Invalid amount")

# emp = Employee()

# print(emp.get_salary())
# emp.set_salary(60000)
# print(emp.get_salary())






# from abc import abstractmethod, ABC

# class Greet(ABC):
#     @abstractmethod
#     def say_hello(self):
#         ...

# class English(Greet):
#     def say_hello(self):
#         return "Helloooo"
    

# g = English()
# print(g.say_hello())


# from abc import abstractmethod, ABC

# class Dog(ABC):  
#     def __init__(self, name):
#         self.name = name

#     @abstractmethod
#     def sound(self): 
#         pass

#     def display_name(self):  
#         print(self.name)

# class Labrador(Dog):
#     def sound(self):
#         print("Woof")

# class Beagle(Dog):  
#     def sound(self):
#         print("Bark")

# dogs = [Labrador("Buddy"), Beagle("Charlie")]

# for dog in dogs:
#     dog.display_name()
#     dog.sound()









# class Cat:
#     def speak(self):
#         return "Meow"

# class Dog:
#     def speak(self):
#         return "Woof"

# def make_animal_speak(animal):
#     return animal.speak()


# print(make_animal_speak(Cat()))
# print(make_animal_speak(Dog()))








# class Vector:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

#     def __add__(self,other):
#         return Vector(self.x+other.x, self.y+other.y)
    

#     def __repr__(self):
#         return f"Vector({self.x}, {self.y})"


# v1 = Vector(2, 3)
# v2 = Vector(4, 5)
# v3 = v1 + v2

# print(v3)






# def is_armstrong(num):
#     digits = len(str(num))
#     temp = num
#     total = 0
    
#     while temp > 0:
#         digit = temp % 10
#         total += digit ** digits
#         temp //= 10
    
#     return total == num

# print(is_armstrong(153))








































