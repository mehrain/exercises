def fib(n=None):
    current_value = 0 
    parent_value = 0
    total_value = 0 
    
    if n == None:
        raise ValueError("Please enter a value")
    elif n == 0: 
        return 0
    elif n == 1: 
        return 1
    else:
        

