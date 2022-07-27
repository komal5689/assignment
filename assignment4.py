# Example 1
from abc import ABC, abstractmethod
class Animal(ABC):
  @abstractmethod
  def eat1(self):
   pass
@abstractmethod
def eat2(self):
   pass
class Tiger(Animal):
 	def eat1(self):
 		print("Tiger implementation ...")
class lion(Tiger):
 	def eat2(self):
 		print("lion implementation ...")
t = lion()
t.eat1()
t.eat2()

"""1)Output
Tiger implementation ...
lion implementation ..."""

# Example 2
from abc import ABC, abstractmethod
class AbstractClassExample(ABC):
     def _init_(self, value):
         self.value = value
         super()._init_()

     @abstractmethod
     def do_something(self):
         pass
 
class DoAdd(AbstractClassExample):
     def do_something(self):
      return self.value + 42
 
class DoMul(AbstractClassExample):
 
     def do_something(self):
         return self.value * 42
 
x = DoAdd(10)
y = DoMul(10)
print(x.do_something())
print(y.do_something())

"""Output
52
420"""


# Example 3
def status(age):
     if age < 0:
         raise ValueError("Only positive integers are allowed")
     if age>22:
         print("eligible for mrg")
     else:
         print("not eligible for mrg try after some time")
try:
     num = int(input("Enter your age: "))
     status(num)
except ValueError:
     print("Only positive integers are allowed you ......")
finally:
     print("finally block....")

"""Output
Enter your age: -9
Only positive integers are allowed you ......
finally block....

Enter your age: 21
not eligible for mrg try after some time
finally block....

Enter your age: 34
eligible for mrg
finally block....
"""


# Example 4
class NegativeAgeException(RuntimeError):
     def _init_(self, age):
         super()._init_()
         self.age = age
def status(age):
         if age < 0:
             raise NegativeAgeException("Only positive integers are allowed")
         if age>22:
             print("Eligible for mrg")
         else:
             print("not Eligible for mrg....")
try:
     num = int(input("Enter your age: "))
     status(num)
except NegativeAgeException:
     print("Only positive integers are allowed")
except:
     print("something is wrong")

"""Output
Enter your age: -6
Only positive integers are allowed

Enter your age: 11
not Eligible for mrg....

Enter your age: 24
Eligible for mrg
"""

# Example 5:
class TooYoungException(Exception):
   def _init_(self,age):
         self.age=age
class TooOldException(Exception):
   def _init_(self,age):
         self.age=age
try:
   age=int(input("Enter Age:"))
   if age<18:
     raise TooYoungException("Plz wait some time ")
   elif age>65:
     raise TooOldException("Your age too old")
   else:
     print("we will find one girl soon")
except TooYoungException as e:
     print("Plz wait some time ")
except TooOldException as e:
     print("Your age too old ")

"""7) Output
Enter Age: 16
Plz wait some time 

Enter Age:20
we will find one girl soon

Enter Age:66
Your age too old"""     


# Example 6
try:
    print("outer try block")
    n = int(input("enter a number"))
    print(10/n)
    try:
        print("inner try")
        print("anu"+"preet")
    except TypeError as e:
        print("Hello")
    else:
     print("inner no exception")
except ArithmeticError as e:
     print(10/5)
else:
     print("outer no excepiton")
finally:
    print("finally block")

"""6)output
outer try block
enter a number"""


# Example 7
class Person(object):
     def _init_(self, first, last):
         self.firstname = first
         self.lastname = last
     def Name(self):
         return self.firstname + " " + self.lastname
class Employee(Person):
    def _init_(self, first, last, staffnum):
        super()._init_(first,last)
        Person._init_(self,first, last)
        self.staffnumber = staffnum
    def GetEmployee(self):
        return self.Name() + ", " + self.staffnumber
x = Person("komal", "addanki")
y = Employee("komal", "addanki", "111")
print(x.Name())
print(y.GetEmployee())

"""7)Output
komal addanki
komal addanki, 111"""


# Example 8
class Person:
     def _init_(self, first, last):
         self.firstname = first
         self.lastname = last
     def _str_(self):
         return self.firstname + " " + self.lastname
class Employee(Person):
 def _init_(self, first, last, id):
         super()._init_(first, last)
         self.id = id
 def _str_(self):
         return super()._str_()+" "+self.id
x = Person("kamalpreet", "gurpreet")
y = Employee("kamalpreet", "gurpreet", "111")
print(x)
print👍

"""8)Output
kamalpreet gurpreet
kamalpreet gurpreet 111"""

# Example 9
class Vehicle:
     def _del_(self):
         print("Vehicle object destroyed")
         print(10/0)
v = Vehicle()
del v

"""9)output
Vehicle object destroyed
    print(10/0)
ZeroDivisionError: division by zero"""

# Example 10
class Customer:
    def _init_(self,name,bal=0.0):
         self.name=name
         self.bal=bal
 
    def deposit(self,amount):
         self.bal=self.bal+amount
    def withdraw(self,amount):
         if amount>self.bal:
             raise RuntimeError("withdraw amount is more than balance")
         else:
             self.bal=self.bal-amount
 
    def remaining(self):
        return self.bal
c = Customer("Komal",10000)
damt = int(input("enter amount to deposit : "))
c.deposit(damt)
amt = int(input("enter amount to withdraw : "))
c.withdraw(amt)
print(c.remaining())

"""10)Output
enter amount to deposit : 90000
enter amount to withdraw : 30000
70000"""