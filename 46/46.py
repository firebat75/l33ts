def solution(nums):
    def backtrack(temp=[], nums2=[]):
        store = nums2.copy()
        print(temp, store)

        if store == []:
            output.append(temp)
            print(f"output: {output}")
            # store = nums.copy()
            # temp = []
        else:
            for i in range(len(store)):
                print(i, temp, store, output)
                backtrack(temp + [store.pop(i)], store)

    output = []
    backtrack([], nums)
    return output


print(solution([1, 2, 3]))
# print(solution([0, 1]))
# print(solution([1]))
