def sortedSquares(nums):
    output = []
    for i in nums:
        output.append(i ** 2)

    output.sort()

    return output
