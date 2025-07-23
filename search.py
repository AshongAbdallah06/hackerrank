from sort import bubble_sort

li = [19, 5, 40, 88, 13, 7, 11]
target = 40


def sequential_search(target, my_list):
    found = False
    for item in range(0, len(my_list)):
        if target == my_list[item]:
            found = True

        if found:
            break

    return True if found else False


def binary_search(target, my_list):
    found = False
    my_sorted_list = bubble_sort(my_list)

    start = 0
    end = len(my_sorted_list) - 1

    while start <= end:
        middle_index = (start + end) // 2

        middle = my_sorted_list[middle_index]

        if target == middle:
            found = True
            break
        elif target < middle:
            end = middle_index - 1
        elif target > middle:
            start = middle_index + 1

    return True if found else False


found = sequential_search(target, li)
print("Sequential: ", end="")
print("Target Found" if found else "Target not found")


print("Binary: ", end="")
found = binary_search(target, li)
print("Target Found" if found else "Target not found")
