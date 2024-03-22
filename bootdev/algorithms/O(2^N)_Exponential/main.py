def power_set(input_set=None):
    if not input_set: 
        input_set = []
    else:
        output_set = []
        for number in range(1, input_set):
            for subset in range(input_set):
                output_set.append(number + subset)
                output_set.append(subset)
        return output_set
                
            
            
        
    
