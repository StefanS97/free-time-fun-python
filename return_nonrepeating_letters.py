def first_non_repeating_letter(text):
    helper_list = []
    dicts = {}

    for i in text.lower():
        if i in dicts:
            dicts[i] += 1
        else:
            dicts[i] = 1
            helper_list.append(i)

    for i in helper_list:
        if dicts[i] == 1:
            variable = i
            index = text.lower().find(variable)
            return text[index]

    return ''