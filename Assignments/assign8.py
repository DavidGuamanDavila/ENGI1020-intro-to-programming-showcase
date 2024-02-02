# -*- coding: utf-8 -*-
"""
Assignment 8 script
Within the class, define the required methods!

@author: lorih
"""

class bankAccount:
    
    balance = 0
    name = ''
    overdraftCount = 0
    
    """
    Initializes bankAccount object
    """
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.overdraftCount = 0
    
    """
    Calculates overdraft due from account and
    subtracts amount from balance
    
    Parameters:
        overdraftCharge - per-transaction fee, >= 0
    Modifies:
        Changes bank balance if needed
    Returns:
        Balance after fees deducted
    """
    def feesCharge(self, overdraftCharge):
        feeAmount = overdraftCharge * self.overdraftCount
        self.balance -= feeAmount
        return self.balance
    
    ###TODO - Implement your methods here!!
    
    def bankAccount(self, name):
        self.name
        self.balance
        return self.name, self.balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            self.overdraftCount += 1
            return self.balance, self.overdraftCount
        else:
            return self.balance
    
    
# # Uncomment code below to do your own testing
# a = bankAccount('a') ##Creates bank account with name a
# print('Create - a should have balance 0: ', a.balance == 0)

# a.deposit(20) ##Deposits $20 into a
# print('Deposit - a should now have balance 20: ', a.balance == 20)

# a.withdraw(10) ##Withdraw $10 from a
# print('Withdraw - a should now have balance 10: ', a.balance == 10)

# a.withdraw(20) ##Withdraw $20 from a, causing overdraft
# print('Withdraw - a should now have balance -10: ', a.balance == -10)
# print('Withdraw - a should now have overdraftCount 1: ', a.overdraftCount == 1)

# ## Calculating overdraft fees
# print('Fees - With 1 overdraft @ $1 each, balance should reduce: ', a.feesCharge(1) == -11)


    
    
        
        
        
        
    
    
    
    


