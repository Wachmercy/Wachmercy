def sort_dicts_by_key(data, key):
    # I want to sort a list of dictionaries based on a key
    # So I will use a simple way by comparing and swapping items
    
    n = len(data)   # get the number of items in the list

    # go through each item
    for i in range(n):
        for j in range(0, n - i - 1):
            # check if the current item is greater than the next one
            if data[j][key] > data[j + 1][key]:
                # swap them if they are in the wrong order
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp

    return data

