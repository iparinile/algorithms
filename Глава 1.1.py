def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = low + high
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 4, 5, 7, 9, 11, 14, 26, 35, 55, 67, 73, 75, 88, 89, 92]
print(binary_search(my_list, 5))
print(binary_search(my_list, 3))
