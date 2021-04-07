def spiralize(number):
    return_value = 1
    for i in xrange(3,5002,2):
        total+=i**2 + (i**2-(i-1)) + (i**2-2*(i-1)) + (i**2-3*(i-1))
    return return_value
