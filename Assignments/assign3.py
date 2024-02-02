balance = float(input('Starting Balance?'))

Type = input('Type d to deposit, w to withdraw or q to quit:')


Amount = float(input('Transaction amount?'))

while balance > 0:

    if Amount > 0:
                
        print('Transaction Successful!')
        
        if Type == 'W' or Type == 'w':
        
            finalBalance = balance - Amount
            print(finalBalance)
            
        
        elif Type == 'D' or Type == 'd':
        
            finalBalance = balance + Amount 
            print(finalBalance)
            
        elif Type == 'Q' or Type == 'q':
            print('Thank you, have a nice day!')
            
    elif Amount < 0:
        
        print('Error negative value. Next time enter a positive value.')
        
        finalBalance = balance
        print(finalBalance)
    


    
 
    

    
    

