#!/bin/python3

# 19 29 30
# 2 28 38
# 89 90 40
# 39 38 29


def flippingMatrix(matrix):
    start = 0
    for m in range(0, len(matrix)):
        for _ in range(0, len(matrix[m])):
            if matrix[m][0] < matrix[m][len(matrix[m]) - 1]:
                matrix[m][0], matrix[m][len(matrix[m]) - 1] = (
                    matrix[m][len(matrix[m]) - 1],
                    matrix[m][0],
                )
                # print(matrix)
                # matrix[m][0] = matrix[m][0]
            # print(m_itr)
        #     print(matrix[m][m_itr])
        # print(matrix[m])

        # print(len(matrix) - 1)
        # end = len(matrix) - 1

        # if matrix[m][0] < matrix[m][0]:
        #     matrix[m][0] = matrix[m][0]

        #     # print(start, end)
        #     start += 1
        #     end -= 1
        # else:
        # ...
        #     print("Not Less")
        # print(start, end)
    # print(matrix)

    return matrix


if __name__ == "__main__":
    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        for m in range(0, len(result) - 1):
            print(result[m])
