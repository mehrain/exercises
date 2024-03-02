def add_format(default_formats, new_format):
    copied_dict = default_formats.copy()
    copied_dict[new_format] = True
    return copied_dict
        


def remove_format(default_formats, old_format):
    copied_dict = default_formats.copy()
    if old_format in default_formats:
        copied_dict[old_format] = False
    return copied_dict