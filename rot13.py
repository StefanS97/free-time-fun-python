import string

def rot13(message):
    encrypted = ''
    lower = string.ascii_lowercase
    translower = lower[13:] + lower[:13]
    upper = string.ascii_uppercase
    transupper = upper[13:] + upper[:13]
    for letter in range(len(message)):
        if message[letter].islower():
            if lower.index(message[letter]) >= 13:
                encrypted += translower[translower.index(message[letter]) + 13]
            else:
                encrypted += lower[lower.index(message[letter])+13]
        elif message[letter].isupper():
            if upper.index(message[letter]) >= 13:
                encrypted += transupper[transupper.index(message[letter]) + 13]
            else:
                encrypted += upper[upper.index(message[letter]) + 13]
        else:
            encrypted += message[letter]

    return encrypted