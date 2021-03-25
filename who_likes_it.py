def likes(names):
    list = names
    if list:
        if len(list) == 1:
            return f'{list[0]} likes this'
        elif len(list) == 2:
            return f'{list[0]} and {list[1]} like this'
        elif len(list) == 3:
            return f'{list[0]}, {list[1]} and {list[2]} like this'
        else:
            return f'{list[0]}, {list[1]} and {len(list)-2} others like this'
    else:
        return 'no one likes this'