def update_dicts(*args):
    result_dict = {}

    for arg in args:
        if arg is not None:
            result_dict.update(arg)
 
    return result_dict