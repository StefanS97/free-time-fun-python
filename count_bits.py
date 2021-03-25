def count_bits(n):
    counter = 0
    while n>0:
        if n%2:
            counter+=1
        n //= 2
    return counter