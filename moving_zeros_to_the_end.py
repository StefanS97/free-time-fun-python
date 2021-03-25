def move_zeros(array):
    helper_array = []
    zeros_counter = 0
    helper_zeros = 0
    for i in range(len(array)):
        if array[i] == 0:
            zeros_counter += 1
        else:
            helper_array.append(array[i])

    if zeros_counter > 0:
        while helper_zeros < zeros_counter:
            helper_array.append(0)
            helper_zeros += 1

    return helper_array