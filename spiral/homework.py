def spiralize(number):
    return_value = 1
    for i in range(3, 502, 2):
        top_right = i**2
        for j in range(4):
            sum += top_right - j * (i - 1)
    return return_value
