overdraftCount = 0

finalBalance = float(input('Starting Balance?'))

Type = input('Type d to deposit, w to withdraw:')



while (Type == 'W' or Type == 'w') or (Type == 'D' or Type == 'd'):
    
    Amount = float(input('Transaction amount?'))

    if Amount > 0 and Type == 'W' or Type == 'w':
                
        print('Transaction Successful!')
        
        finalBalance = finalBalance - Amount
        
        if finalBalance < 0.0:
            
            overdraftCount = overdraftCount + 1
            
            print(overdraftCount)
            
        print(finalBalance)
          
            
    elif Amount > 0 and Type == 'D' or Type == 'd':
        
        finalBalance = finalBalance + Amount
            
        print(finalBalance)
        
        
    Type = input('Type d to deposit, w to withdraw or q to quit:')  
    

