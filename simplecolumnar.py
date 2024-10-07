import random

x = True  

    message = input("enter message ") 
    key = input("ehat is your key")  
    random.seed(str(key))
    
    r = random.sample(message, len(message))
    
    print(r)