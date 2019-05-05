# Object Oriented Programming Challenge
For this challenge, create a bank account class that has two attributes:
- owner
- balance

and two methods:
- deposit
- withdraw

As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

```py
class Account:
	
	def __init__(self, owner, balance):
		self.owner = owner
		self.balance = balance

	def __str__(self):
		return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'

	def deposit(self, amount):
		self.balance += amount
		return 'Deposit Accepted'

	def withdraw(self, amount):
		if amount <= self.balance:
			self.balance -= amount
			return 'Withdrawal Accepted'
		else:
			return 'Funds Unavailable!'
```
```sh
# 1. Instantiate the class
acct1 = Account('Jose',100)
```
```sh
# 2. Print the object
print(acct1)
Account owner:   Jose
Account balance: $100
```
```sh
# 3. Show the account owner attribute
acct1.owner
'Jose'
```
```sh
# 4. Show the account balance attribute
acct1.balance
100
```
```sh
# 5. Make a series of deposits and withdrawals
acct1.deposit(50)
Deposit Accepted
acct1.withdraw(75)
Withdrawal Accepted
```
```sh
# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)
Funds Unavailable!
```
## Good job!