from itertools import zip_longest

def get_min_len(*args):
    for index, item in enumerate(args):
        if index == 0:
            min_len = len(item)
        elif min_len > len(item):
            min_len = len(item)
    return min_len

def sum_lists(*lists, mode="s"):
    match mode:
        case "s":
            zipped_list = zip(*lists)
        case "l":
            zipped_list = zip_longest(*lists, fillvalue=0)
        case _:
            raise TypeError("Only 's' and 'l' are accepted as modes")
        
    return [sum(i) for i in zipped_list]