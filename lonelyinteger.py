def lonelyinteger(a):
    item_counter = 0
    for item in a:
        item_counter = 0
        for j in a:
            if item == j:
                item_counter += 1

        if item_counter == 1:
            return item


if __name__ == "__main__":
    n = int(input().strip())

    numbers = []

    for _ in range(0, n):
        a = input()

        for num in a.split():
            numbers.append(int(num))

    result = lonelyinteger(numbers)
