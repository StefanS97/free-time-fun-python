def duplicate_count(text):
    dictionary = {}
    white_space = text.replace(' ', '').lower()
    s = set(white_space)
    l = list(s)
    count = 0

    for i in range(len(l)):
        dictionary.update({l[i]: 0})

    for i in range(len(white_space)):
        if white_space[i] in dictionary:
            dictionary[white_space[i]] += 1

    for i in dictionary.values():
        if i >= 2:
            count += 1

    return count
