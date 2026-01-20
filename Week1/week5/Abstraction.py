# Abstraction


''' Question 1: Class Inheritance and Method Overriding
 Create a class employee eith the following:
Attributes : name, salary
Method: get_annual_salary() that returns the yeraly salary
create a subclass manager that:
adds on attributes bonus
Overrides get_annual_salary() to inlcude bonus
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus
    def get_annual_salary(self):
        return super().get_annual_salary() + self.bonus

# Test
emp = Employee("Alice", 5000)
print(emp.get_annual_salary())  # 60000

mgr = Manager("Bob", 7000, 10000)
print(mgr.get_annual_salary())

'''


#
# from abc import (ABC)
#
# class Employee(ABC):
#     @abstractmethod
#     def __init__self(self,name,salary):
#         self.name = name
#         self.salary = salary
#
#     def get_annual_salary(self):
#         return self.salary * 12
#
# class Manager(Employee):
#     def __init__(self,name,salary,bonus):
#         super().__init__(name,salary)
#         self.bonus = bonus
#
#     def get_annual_salary(self):
#         return self.salary * 12 + self.bonus
#
# emp = Employee("Bikesh" , 15000 )
# mgr = Manager("Shakya", 16000, 5000)
# print(f"{emp.name}'s annual salary : ${emp.get_annual_salary()} ")
# print(f"{mgr.name}'s annual salary : ${emp.get_annual_salary()} ")

'''Qn 2
Encapsulation and property Decorter
Create a class BankAccount That:

Has a private attribute __balance

Has methods deposit (amount and withdraw(amount)

prevemts withdrals if the amoutn is f=greateer tahn tht balance

use @property to create a read only attributes balance

implement the class and show how encapsulation and property decorator
'''
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit must be positive.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Withdrawal denied: Insufficient balance")
        elif amount <= 0:
            print("Withdrawal must be positive.")
        else:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")

    @property
    def balance(self):

        return self.__balance
