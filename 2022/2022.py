def construct2DArray(original, m, n):

    output = []

    if len(original) != m * n:
        return output

    index = 0

    for row in range(m):
        output.append([])
        for col in range(n):
            output[row].append(original[index])
            index += 1

    return output


print(construct2DArray([1, 2, 3, 4], 2, 2))
print(construct2DArray([1, 2, 3], 1, 3))
print(construct2DArray([1, 2], 1, 1))
