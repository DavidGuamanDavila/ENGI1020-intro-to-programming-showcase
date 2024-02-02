# Some parts of this script have been taken from assignment 3 and 4.

def setStartingBalance():
    balance = float(input('Starting Balance?'))
    return balance
  

def depositAmount(amount, balance):
    if amount >= 0: 
        newBalance = balance + amount
        return newBalance
    
    elif amount < 0:
        newBalance = balance
        
        print("Negative value, sorry. Try again.")
        return newBalance
        

def withdrawAmount(amount, balance):
    if amount >= 0: 
            newBalance = balance - amount
            overdraftCount = 0
            
            if newBalance < 0.0:
                overdraftCount = True
                
            elif newBalance > 0.0:
                overdraftCount = False
            
            return newBalance, overdraftCount
           
            
    elif amount < 0:
            newBalance = balance
            overdraftCount = 0
            
            if newBalance < 0.0:
                overdraftCount = True
                
            elif newBalance > 0.0:
                overdraftCount = False
            
            print("Negative value, sorry. Try again")
            return newBalance, overdraftCount
    
Type = input('Hello! To proceed type d to deposit or w to withdraw:')

while (Type == 'W' or Type == 'w') or (Type == 'D' or Type == 'd'):

    if Type == 'W' or Type == 'w':
    
        amount = float(input('What is your transaction amount?'))
       
        outputwithdraw = withdrawAmount(amount,setStartingBalance())
        
        print(outputwithdraw)
       
    elif Type == 'D' or Type == 'd':
        
        amount = float(input('What is your transaction amount?'))
        
        outputdeposit = depositAmount(amount,setStartingBalance())
        
        print(outputdeposit)
        
    Type = input('Type d to deposit, w to withdraw or any key to quit:')