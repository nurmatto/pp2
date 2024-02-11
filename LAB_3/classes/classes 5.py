# who's gonna carry the boats and the logs?!

class Bank_Account:
	def __init__(self, owner, balance=0):
		self.owner = owner
		self.balance = balance
		
	def deposit(self, money_amount):
		if money_amount > 0:
			self.balance +=money_amount
			print('Ваш счет был пополнен на сумму',money_amount)
			print('Ваш измененный баланс равен',self.balance)
		else:
			print('Ошибка, операция невозможна')
			
	def withdraw(self, money_amount):
		if 0 < money_amount <= self.balance:
			self.balance -=money_amount
			print('Из вашего баланса была списана сумма', money_amount)
			print('Ваш измененный баланс равен',self.balance)
		else:
			print('Ошибка, операция невозможна')
owner_1 = Bank_Account('Nurmukhamed Torebek')
owner_1.deposit(10000)
owner_1.withdraw(5000)