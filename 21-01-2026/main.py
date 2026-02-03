# class Person:
#     def __init__(self):
#         self.__name = "ABC"
#         self.__age = 10
#         self.__marks = []

#     def get_name(self):
#         return self.__name
    
#     def get_age(self):
#         return self.__age
    
#     def set_name(self, name):
#         self.__name = name
    
#     def set_age(self, age):
#         self.__age = age

#     def set_marks(self,**kwargs):
#         for subject, marks in kwargs.items():
#             self.__marks.append({subject:marks})

#     def get_marks(self):
#         return self.__marks

# p1 = Person()
# print(p1.get_name())
# print(p1.get_age())

# p1.set_name("XYZ")
# p1.set_age(25)

# print(p1.get_name())
# print(p1.get_age())

# p1.set_marks(maths=90,civics=80,history=78,geography=79,english=90)
# print(p1.get_marks())








# from abc import abstractmethod,ABC

# class Shape(ABC):
#     def __init__(self, c):
#         self.color = c

#     def get_color(self):
#         return self.color

#     @abstractmethod
#     def get_area(self):
#         pass

# class Square(Shape):
#     def __init__(self, c, side):
#         super().__init__(c)  
#         self.side = side

#     def get_area(self):
#         return self.side * self.side

#     def get_perimeter(self):
#         return self.side *4
    
#     def get_natural_no(self,n):
#         for i in range(1,n+1):
#             print(i, end=" ")
    
# s1 = Square("red",5.0)
# print(s1.get_color())
# print(s1.get_area())
# print(s1.get_perimeter())
# s1.get_natural_no(12)








# def missing_number(arr):
#     n=arr[-1]
#     my_sum = (n*(n+1))//2
#     return my_sum-sum(arr)
    






# my_list = []
# while True:
#     n = input()
#     if n == "STOP":
#         break
#     else:
#         my_list.append(int(n))

# print(missing_number(my_list))










# class Employee:
#     def __init__(self,id,salary):
#         self.id=id
#         self.salary=salary

# class SalesEmployee(Employee):
#     def __init__(self, id, salary,sales):
#         super().__init__(id, salary)
#         self.sales = sales

#     def get_details(self):
#         print(f"ID: {self.id} \nSalary: {self.salary} \nSales: {self.sales}")
    
# id = int(input("Enter id: "))
# salary = float(input("enter salary: "))
# sales = float(input("enter sales: "))
# s1 = SalesEmployee(id,salary,sales)
# s1.get_details()









# class Student:
#     def __init__(self,s_id,d_id,**kwargs):
#         self.s_id = s_id
#         self.d_id = d_id
#         super().__init__(**kwargs)

#     def get_info(self):
#         print(f"Student ID: {self.s_id} Department ID: {self.d_id}")

# class Faculty:
#     def __init__(self, e_id, d_id,**kwargs):
#         self.e_id = e_id
#         self.d_id = d_id
#         super().__init__(**kwargs)
    
#     def get_info(self):
#         print(f"Employee ID: {self.s_id} Department ID: {self.d_id}")

# class PhdStudent(Student, Faculty):
#     def __init__(self, s_id, d_id,e_id):
#         super().__init__(s_id=s_id, d_id=d_id, e_id=e_id)
    
#     def get_info(self):
#         print(f"Student ID: {self.s_id} Employee ID: {self.e_id} Department ID: {self.d_id}")


# p1 = PhdStudent(101,55,42)
# p1.get_info()

















# class Student:
#     def __init__(self, std, deptid):
#         self.std = std
#         self.deptid = deptid
        
#     def get_info(self):
#         return f'Student ID: {self.std} Dept ID: {self.deptid}'
    
# class Faculty:
#     def __init__(self, eid, deptid):
#         self.eid = eid
#         self.deptid = deptid
        
#     def get_info(self):
#         return f'Employee ID: {self.eid} Department ID: {self.deptid}'
    
# class PhdStudent(Student, Faculty):
#     def __init__(self, sid, eid, deptid):
#         Student.__init__(self, sid, deptid)
#         Faculty.__init__(self, eid, deptid)
    
#     def get_info(self):
#         return f'Student ID: {self.std}\nEmployee ID: {self.eid}\nDepartment ID: {self.deptid}'
    
# person1 = PhdStudent(1,5,100)
# print(person1.get_info())








# n = int(input())
# temp = []
# for i in range(n):
#     temp.append(int(input()))

# print(temp[::-1])






# class ComplexNumber:
#     def __init__(self, real, imaginary):
#         self.real = real
#         self.imaginary = imaginary

#     def __add__(self,other):
#         real_part = self.real + other.real
#         imaginary_part = self.imaginary + other.imaginary
#         return ComplexNumber(real_part, imaginary_part)

#     def __str__(self):
#         return f"{self.real} + {self.imaginary}i"
    

# c1 = ComplexNumber(2,4)
# c2 = ComplexNumber(4,6)

# c3 = c1+c2
# print(c3)



    




# class A:
#     def show(self):
#         print("Class A")
    
# class B(A):
#     def show(self):
#         print("Class B")
        
# class C(A):
#     def show(self):
#         print("Class C")
        
# class D(B, C):
#     pass

# d = D()
# d.show()









# n = int(input())

# grid = []
# for i in range(n):
#     row = list(map(int, input().split()))
#     grid.append(row)

# primary_diag = 0
# secondary_diag = 0


# for i in range(n):
#     primary_diag += grid[i][i]
#     secondary_diag += grid[i][n-1-i]

# print(primary_diag)
# print(secondary_diag)


# from abc import ABC, abstractmethod

# class Bank(ABC):

#     @abstractmethod
#     def interest_calc(self, amount, years):
#         ...

# class SBI(Bank):
#     def interest_calc(self, amount, years):
#         rate = 0.05
#         return amount * rate * years

# class HDFC(Bank):
#     def interest_calc(self, amount, years):
#         rate = 0.07
#         return amount * rate * years
        
# class ICICI(Bank):
#     def interest_calc(self, amount, years):
#         rate = 0.09
#         return amount * rate * years



# abc = SBI()
# print(abc.interest_calc(10000,5))



    
# m,n = map(int, input().split())
# max_lev = []
# for i in range(m):
#     levels = list(map(int,input().split()))
#     max = 0
#     for level in levels:
#         if level > max:
#             max = level
#     max_lev.append(max)

# print(max_lev)





# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)

# a, b = map(int, input().split())
# print(gcd(a, b))






# n = int(input())

# result = []
# present_spread = 2  

# result.append(present_spread)

# for i in range(2,n+1):
#     present_spread += (i-1)*13
#     result.append(present_spread)


# print(result)









# n = int(input("Enter next n values: "))
# result = []

# if n == 1:
#     result.append(1)
# elif n == 2:
#     result.append(1)
#     result.append(3)
# else:
#     result = [1,3]

#     sum = result[0] + result[1]
#     result.append(sum)
    
#     for i in range(3,n):
#         sum = result[i-1] + result[i-2] + result[i-3]
#         result.append(sum)
        
#     print(result)



def tower_of_hanoi(n, src, med, dest):
    if n == 1:
        print(f"Move disk 1 from {src} to {dest}")
        return

    tower_of_hanoi(n-1, src, dest, med)

    print(f"Move disk {n} from {src} to {dest}")


    tower_of_hanoi(n-1, med, src, dest)


n = int(input("Enter number of disks: "))
tower_of_hanoi(n, "A", "B", "C")






n = int(input())


for i in range(n, 0, -2):
    spaces = (n - i) // 2
    print("  " * spaces + "* " * i)

