def miniMaxSum(arr):
    sum_of_values = 0
    min_value = 0
    max_value = 0

    for i in range(0, len(arr)):
        values = list()

        for item in arr:
            values.append(item)
        values.remove(arr[i])

        sum_of_values = 0
        for v in values:
            sum_of_values += v

        if not min_value:
            min_value = sum_of_values

        if sum_of_values > max_value:
            max_value = sum_of_values
        else:
            if sum_of_values < min_value:
                min_value = sum_of_values
    print(f"{min_value} {max_value}")


if __name__ == "__main__":
    text = "5 5 5 5 5"
    number_array = []

    for num in text.split():
        number_array.append(int(num))

    miniMaxSum(number_array)
