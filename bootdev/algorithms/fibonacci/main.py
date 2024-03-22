def fib(n=None):
    if n == None:
        raise ValueError("Please enter a value")
    elif n == 0: 
        return 0
    elif n == 1: 
        return 1
    else:
        current_value = 0 
        parent_value = 1
        for _ in range(n - 1):
            current_value, parent_value = parent_value, current_value + parent_value
        return parent_value
        
        

