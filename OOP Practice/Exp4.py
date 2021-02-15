#4.	Define a class Account with static variable rate_of_interest, instance variables balance and account number.
# Make functions to set values in instance object of Account, show balance,
# show rate of interest, withdraw and deposit. 
class Account:
    def __init__(self, rate_of_interest, account_number):
        self.rate_of_interest = rate_of_interest
        self.balance = 10000
        self.account_number = account_number

    def __repr__(self):
        return f"{self.account_number} - {self.balance}"

    @property
    def account(self):
        return f"{self.account_number} - {self.balance}"
    
    @account.setter
    def account_show(self, show_balance, show_rate_of_interest):
        self.balance = show_balance
        self.rate_of_interest = show_rate_of_interest

    def deposit(self, amount):
        prev_bal = self.balance
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
            prev_bal = self.balance
            self.balance -= amount
            return f"{self.balance}"
    
ICICI = Account("15%", 1500015459)

print(f"Balance:{ICICI.balance}\nRate of Interest:{ICICI.rate_of_interest}\nDeposit:{ICICI.deposit(5000)}\nWithdraw:{ICICI.withdraw(3000)}")