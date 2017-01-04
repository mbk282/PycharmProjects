import math

def log_add(a, b):
    '''Adds to numbers in their logarithmic transformtions.

    :param a: The first logarithmically transformed number.
    :param b: The second logarithmically transformed number.
    :return: The log-sum of the two numbers
    '''
    if a == -math.inf:
        if b ==-math.inf:
            return -math.inf
        else:
            return b
    elif b == -math.inf:
        return a
    elif a > b:
        return a + math.log1p(math.exp(b-a))
    else:
        return b + math.log1p(math.exp(a-b))

def log_add_list(list_of_numbers):
    '''Adds all the logarithmically transformed numbers in a list.

    :param list_of_numbers: A list of logarithmically transformed numbers.
    '''
    x = -math.inf
    list_of_numbers.sort()
    for i in list_of_numbers:
        x = log_add(x, i)
    return(x)

def log_subtract(a , b):
    '''Subtracts a logarithmically transformed number b from another such number a.

    :param a: The first logarithmically transformed number.
    :param b: The second logarithmically transformed number.
    :return: The log-difference between a and b
    '''
    if a == 0:
        if b ==0:
            return -math.inf
        else:
            return b
    elif b == 0:
        return a
    elif a > b:
        return a + math.log1p(-math.exp(b-a))
    else:
        return b + math.log1p(-math.exp(a-b))



def log_subtract_list(list_of_numbers):
    '''Subtracts all the logarithmically transformed numbers in a list from the first one.

    :param list_of_numbers: A list of logarithmically transformed numbers.
    '''
    list_of_numbers.sort()
    x = list_of_numbers[0]
    for i in range(1, len(list_of_numbers)):
        x = log_subtract(x, list_of_numbers[i])
    return (x)

