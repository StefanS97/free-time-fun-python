from string import digits as d, ascii_letters as l, punctuation as p

def check(pw):
    digitcount = 0
    lettercount = 0
    punctcount = 0

    if len(pw) >= 8:
        for letter in range(len(pw)):
            if pw[letter] in l:
                lettercount += 1
            elif pw[letter] in d:
                digitcount += 1
            elif pw[letter] in p:
                punctcount += 1
            else:
                return 'Contains white spaces'
                break

        if digitcount >= 1 and lettercount >= 1 and punctcount >= 1:
            return 'Password Accepted'
        else:
            return 'Something is missing'

    else:
        return 'Password too short'