"""

1. pass statement acts as empty statement in python
2. it acts as a placeholder to implement future code
3. it is used to define minimal classes and functions
4. to define abstract methods, pass statement is the best choice

"""

from abc import ABC, abstractmethod


def f1():
	pass


class A:
	pass


class B:
	pass


class C:
	pass


x = 10
if x >= 35:
	print('success')
else:
	pass


class Loan(ABC):
	
	@abstractmethod
	def get_interest_rate(self):
		pass


class HomeLoan(Loan):
	
	def get_interest_rate(self):
		return 8.0


class VehicleLoan(Loan):
	
	def get_interest_rate(self):
		return 11.0


class PersonalLoan(Loan):
	
	def get_interest_rate(self):
		return 15.0
