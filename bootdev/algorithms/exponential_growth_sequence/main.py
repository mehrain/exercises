def exponential_growth(n, factor, days):
    growth_list = []
    growth_list.append(n)
    
    for i in range(days):
        growth_list.append(growth_list[i] * factor)
    return growth_list
        
