def check_str_and_execute(function):
    def intern_function(str):
        is_string(str)
        return function(str)
    return intern_function


@check_str_and_execute
def invert_string(str):
    return str[::-1]


def is_string(x):
    if not isinstance(x,str):
        raise TypeError("the argument isn't str")


print(invert_string("Caio"))