def count_names(list_of_lists, target_name):
    name_counted = 0 
    for list in list_of_lists:
        for names in list: 
            if names == target_name:
                name_counted += 1
    return name_counted