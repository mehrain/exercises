def zipmap(keys, values):
    empty_dict = {}
    if len(keys) > len(values):
        return
    empty_dict = map(zip(keys, values))
    
    
'''
def zipmap(keys, values):
    if len(keys) > len(values):
        return
    return dict(map(lambda key, value: (key, value), keys, values))
'''