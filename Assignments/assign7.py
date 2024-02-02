# Some parts of this script have been taken from assignment 6.

balances = {
        "David": 3,
        "Daniel": 50,
        "Silvana": 20
        }

def withdrawMoney(name, amount):
    
    if name in balances.keys():
        overdraftCount = 0
        nameveri = True
        balances[name]-= amount
        amount = balances[name]
        
        if amount < 0.0:
                overdraftCount = True
                
        else:
                overdraftCount = False
                
        return nameveri, overdraftCount,  amount 
        
    else:
        nameveri = False 
        amount = 0    
        overdraftCount = True
        balances[name]= 0
        
        
    return  nameveri, overdraftCount, amount     

def depositMoney(name, amount):
    if name in balances.keys(): 
        nameveri = True
        balances[name]+= amount
        amount = balances[name]
        
    else:
        balances[name]= amount
        nameveri = False
             
    return nameveri, amount  
    
Type = input('Type d to deposit, w to withdraw or any key to quit:')


if Type == 'W' or Type == 'w':
    name = input('What is your first name')
    amount = float(input('What is your transaction amount?'))
    outputwithdraw = withdrawMoney(name, amount)  
    print(outputwithdraw)
          
elif Type == 'D' or Type == 'd':
    name = input('What is your first name')
    amount = float(input('What is your transaction amount?'))
    outputdeposit = depositMoney(name, amount)
    print(outputdeposit)
        
print(balances)
