def power_set(input_set):
    if len(input_set) == 0:
        return [[]]

    first_element = input_set[0]
    remaining_set = input_set[1:]
    subsets = power_set(remaining_set)

    output_set = []
    for subset in subsets:
        output_set.append([first_element] + subset)
        output_set.append(subset)
        
    return output_set

                
                
                


            
            
        
    
