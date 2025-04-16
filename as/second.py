def repair_list(lst):
    for i in range(len(lst)):
        if lst[i] is not None:
            for j in range(i):
                lst[j] = lst[i]
            break

    # Replace remaining None values with previous non-None
    for i in range(1, len(lst)):
        if lst[i] is None:
            lst[i] = lst[i - 1]

    return lst

data = [None, None, 2, 3, None, 5, None, None]
print(repair_list(data))  