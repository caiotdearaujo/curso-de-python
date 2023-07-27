def pause_function(function, x):
    def paused_function(y):
        return function(x,y)
    return paused_function


def sum(x,y):
    return x+y


def multiply(x,y):
    return x*y


sum_with_5 = pause_function(sum,5)
multiply_by_10 = pause_function(multiply,10)

print(sum_with_5(5))
print(multiply_by_10(10))