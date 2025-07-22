def diagonalDifference(arr):
    start = 0
    end = len(arr) - 1

    left_diagonal_sum = 0
    right_diagonal_sum = 0

    for i in range(0, len(arr)):
        left_diagonal_sum += arr[i][start]
        right_diagonal_sum += arr[i][end]

        start += 1
        end -= 1

    difference = left_diagonal_sum - right_diagonal_sum

    return abs(difference)


if __name__ == "__main__":
    arr = [
        [6, 6, 7, -10, 9, -3, 8, 9, -1],
        [9, 7, -10, 6, 4, 1, 6, 1, 1],
        [-1, -2, 4, -6, 1, -4, -6, 3, 9],
        [-8, 7, 6, -1, -6, -6, 6, -7, 2],
        [-10, -4, 9, 1, -7, 8, -5, 3, -5],
        [-8, -3, -4, 2, -3, 7, -5, 1, -5],
        [-2, -7, -4, 8, 3, -1, 8, 2, 3],
        [-3, 4, 6, -7, -7, -8, -3, 9, -6],
        [-2, 0, 5, 4, 4, 4, -3, 3, 0],
    ]

    result = diagonalDifference(arr)

    print(result)
