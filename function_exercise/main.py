def multiplicar(*args):
    for index, item in enumerate(args):
        if index:
            produto *= item
        else:
            produto = item
    
    return produto


def e_par(x):
    if x % 2:
        return False
    return True