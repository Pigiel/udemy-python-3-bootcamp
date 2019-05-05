#!/usr/bin/env python3

class Account:

	def __init__(self, owner, balance):
		self.owner = owner
		self.balance = balance

	def __str__(self):
		return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'
		#return 'Account owner:   {}\nAccount balance: ${}'.format(self.owner, self.balance)

	def deposit(self, amount):
		self.balance += amount
		return 'Deposit Accepted'

	def withdraw(self, amount):
		if amount <= self.balance:
			self.balance -= amount
			return 'Withdrawal Accepted'
		else:
			return 'Funds Unavailable!'

print('\n# 1. Instantiate the class')
print("acct1 = Account('Jose',100)")
acct1 = Account('Jose',100)
print('\n# 2. Print the object')
print('print(acct1)')
print(acct1)
print('\n# 3. Show the account owner attribute')
print('acct1.owner')
print(acct1.owner)
print('\n# 4. Show the account balance attribute')
print('acct1.balance')
print(acct1.balance)
print('\n# 5. Make a series of deposits and withdrawals')
print('acct1.deposit(50)')
print(acct1.deposit(50))
print('acct1.withdraw(75)')
print(acct1.withdraw(75))
print('\n# 6. Make a withdrawal that exceeds the available balance')
print('acct1.withdraw(500)')
print(acct1.withdraw(500))