def find_last_name(names_dict=None, first_name=None):
    if first_name not in names_dict: 
        return None
    else: 
        return names_dict[first_name]
