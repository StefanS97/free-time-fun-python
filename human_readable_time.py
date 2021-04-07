def make_readable(seconds):
    if seconds >= 0 and seconds <= 359999:
        hrs = seconds // 3600
        seconds %= 3600
        mins = seconds // 60
        seconds %= 60
        secs = seconds
        hour = str('{:02d}'.format(hrs))
        minute = str('{:02d}'.format(mins))
        second = str('{:02d}'.format(secs))
        time = f"{hour}:{minute}:{second}"

        return time