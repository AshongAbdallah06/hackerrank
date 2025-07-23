def bubble_sort(n):
    # print("Bubble Sort:")
    for _ in range(0, len(n) - 1):
        swapped = False
        for index in range(0, len(n) - 1):
            if n[index] > n[index + 1]:
                n[index + 1], n[index] = n[index], n[index + 1]
                swapped = True

        if not swapped:
            break
    return n


def selection_sort(n):
    # print("Selection Sort:")
    for j in range(0, len(n) - 1):
        smallest_element = n[j]

        for i in range(0, len(n)):
            if n[i] < smallest_element:
                smallest_element = n[i]

        if smallest_element != j:
            n[smallest_element] = n[j]

        print(n)


def main():
    li = [19, 5, 40, 88, 13, 7, 11]
    print(f"Original: {li}")

    sorted_list = bubble_sort(li)
    print(sorted_list)


if __name__ == "__main__":
    main()
# selection_sort(li)
