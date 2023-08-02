def get_min_len(*args):
    for index, item in enumerate(args):
        if index == 0:
            min_len = len(item)
        elif min_len > len(item):
            min_len = len(item)
    return min_len

def sum_lists(*lists):
    interval = get_min_len(*lists)

    result_list = []
    for i in range(interval):
        result = 0
        for l in lists:
            result += l[i]
        result_list.append(result)
    
    return result_list