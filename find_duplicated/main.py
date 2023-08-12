def find_duplicated(x: list):
    already_seen = set()

    for i in x:
        if i in already_seen:
            return i
        already_seen.add(i)
    return -1

list = [1,2,3,]
print(find_duplicated(list))