def solution(nums, k):
    freqs = {}

    for num in nums:
        if num not in freqs:
            freqs[num] = 1
        else:
            freqs[num] += 1

    output = []
    for num in range(k):
        x = max(freqs, key=freqs.get)
        output.append(x)
        freqs[x] = 0

    return output


print(solution([1, 1, 1, 2, 2, 3], 2))
print(solution([1], 1))
