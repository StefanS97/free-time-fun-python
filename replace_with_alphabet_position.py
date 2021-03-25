def alphabet_position(text):
    letter = text.lower()
    lists = list(letter)
    helper = []
    string = ' '

    for i in range(len(lists)):
        if lists[i] == 'a':
            helper.append('1')
        if lists[i] == 'b':
            helper.append('2')
        if lists[i] == 'c':
            helper.append('3')
        if lists[i] == 'd':
            helper.append('4')
        if lists[i] == 'e':
            helper.append('5')
        if lists[i] == 'f':
            helper.append('6')
        if lists[i] == 'g':
            helper.append('7')
        if lists[i] == 'h':
            helper.append('8')
        if lists[i] == 'i':
            helper.append('9')
        if lists[i] == 'j':
            helper.append('10')
        if lists[i] == 'k':
            helper.append('11')
        if lists[i] == 'l':
            helper.append('12')
        if lists[i] == 'm':
            helper.append('13')
        if lists[i] == 'n':
            helper.append('14')
        if lists[i] == 'o':
            helper.append('15')
        if lists[i] == 'p':
            helper.append('16')
        if lists[i] == 'q':
            helper.append('17')
        if lists[i] == 'r':
            helper.append('18')
        if lists[i] == 's':
            helper.append('19')
        if lists[i] == 't':
            helper.append('20')
        if lists[i] == 'u':
            helper.append('21')
        if lists[i] == 'v':
            helper.append('22')
        if lists[i] == 'w':
            helper.append('23')
        if lists[i] == 'x':
            helper.append('24')
        if lists[i] == 'y':
            helper.append('25')
        if lists[i] == 'z':
            helper.append('26')

    return string.join(helper)


# I really could have done it better, I know.