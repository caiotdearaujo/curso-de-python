def zip_smallest(list1, list2):
    interval = min(len(list1), len(list2))
    return [
        (list1[i], list2[i])
        for i in range(interval)
    ]

def zip_longest(list1, list2):
    interval = max(len(list1), len(list2))
    result = []
    for i in range(interval):
        if len(list1) <= i:
            result.append((None,list2[i]))
            continue
        if len(list2) <= i:
            result.append((list1[i],None))
            continue
        result.append((list1[i],list2[i]))
        
    return result