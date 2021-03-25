def square_digits(num):
    number = (list(str(num)))
    helper = ''

    for i in range(len(number)):
        square = int(number[i]) * int(number[i])
        helper += str(square)

    return int(helper)