def does_name_exist(first_names, last_names, full_name):
    counter = 0
    max_length = (len(first_names) * len(last_names))
    for first_name in first_names:
        for last_name in last_names:
            if (first_name + " " + last_name) in full_name:
                return True
            else:
                counter += 1 
    if counter == max_length: #assignment notes length of fist/last is always equal so i dont have to handle that. 
        return False 