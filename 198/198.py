def solution(nums):
    def backtracking(path, nums):
        print(path, nums)
        if not nums and path > sum(output[0]):
            print("appended")
            output[0] = [path]
        else:
            for i in range(len(nums)):
                print(i, path, nums)
                if len(nums) > 1:
                    backtracking(path + nums[i], nums[i + 2 :])
                else:
                    backtracking(path + nums[i], [])

    output = [[0]]
    backtracking(0, nums)
    return output[0][0]


print(solution([1, 2, 3, 1]))
print(solution([2, 7, 9, 3, 1]))
print(
    solution(
        [
            183,
            219,
            57,
            193,
            94,
            233,
            202,
            154,
            65,
            240,
            97,
            234,
            100,
            249,
            186,
            66,
            90,
            238,
            168,
            128,
            177,
            235,
            50,
            81,
            185,
            165,
            217,
            207,
            88,
            80,
            112,
            78,
            135,
            62,
            228,
            247,
            211,
        ]
    )
)
