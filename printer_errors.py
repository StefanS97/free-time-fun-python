def printer_error(s):
    lower_case = s.lower()
    errors = 0
    total_count = 0
    for i in range(len(lower_case)):
        ch = ord(lower_case[i])
        if ch < 97 or ch > 109:
            errors += 1
        total_count += 1

    return f'{errors}/{total_count}'