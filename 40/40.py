# def solution(candidates, target):
#     if sum(candidates) < target:
#         return []

#     candidates.sort()
#     output = []

#     i = 0
#     while i < len(candidates):
#         if candidates[i] >= target:
#             if candidates[i] == target:
#                 output.append([candidates[i]])
#                 candidates = candidates[:i]
#             else:
#                 candidates = candidates[:i]
#         i += 1

#     # print(candidates)

#     i = 0
#     a = True
#     while a and len(candidates) > 1:
#         # print(i)
#         if candidates[i] + candidates[0] >= target:
#             if candidates[i] + candidates[0] > target:
#                 candidates = candidates[:i]
#             else:
#                 output.append([candidates[0], candidates[i]])
#                 candidates = candidates[:i]
#             a = False

#         i += 1
#         if i > len(candidates) - 1:
#             a = False

#     # print(candidates)

#     def remove_overdupes():
#         singles = list(dict.fromkeys(candidates))

#         for item in singles:
#             print(item)
#             strt = candidates.index(item)
#             i = strt
#             count = 0
#             while candidates[i] == candidates[strt] and i < len(candidates) - 1:
#                 print(item, strt, i, count)
#                 i += 1
#                 count += item

#             print(count, target)

#             if count > target:
#                 f = (count - target) // item
#                 print(f)
#                 candidates[strt:i] = candidates[strt : i - f - 1]

#     remove_overdupes()

#     # print("Dqdwqdwq", candidates)

#     if sum(candidates) == target:
#         print("PERFECT")
#         output.append(candidates)
#         return output

#     def backtracking(path, candidates):
#         path.sort()
#         if sum(path) == target and path not in output:
#             output.append(path)
#         elif sum(path) > target:
#             pass
#         else:
#             for i in range(len(candidates)):
#                 # print(path, candidates)
#                 backtracking(
#                     path + [candidates[i]], candidates[:i] + candidates[i + 1 :]
#                 )

#     backtracking([], candidates)
#     return output


# # print(solution([5, 2, 1, 1, 4, 2, 1], 3))
# print(
#     solution(
#         [
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#             1,
#         ],
#         30,
#     )
# )
# # print(solution([10, 1, 2, 7, 6, 1, 5], 8))
# # print(solution([2, 5, 2, 1, 2], 5))
# # print(
# #     solution(
# #         [
# #             15,
# #             20,
# #             11,
# #             26,
# #             13,
# #             30,
# #             31,
# #             27,
# #             8,
# #             27,
# #             6,
# #             28,
# #             22,
# #             12,
# #             17,
# #             9,
# #             8,
# #             21,
# #             12,
# #             21,
# #             15,
# #             25,
# #             7,
# #             23,
# #             15,
# #             23,
# #             24,
# #             28,
# #             28,
# #             17,
# #             11,
# #             30,
# #             24,
# #             9,
# #             13,
# #             33,
# #             26,
# #             10,
# #             25,
# #             22,
# #             24,
# #             27,
# #             15,
# #             11,
# #             34,
# #             19,
# #             15,
# #             29,
# #             6,
# #             14,
# #             15,
# #             8,
# #             5,
# #             9,
# #             18,
# #             15,
# #             28,
# #             30,
# #             9,
# #             13,
# #             34,
# #             7,
# #             30,
# #         ],
# #         28,
# #     )
# # )


def solution(self, candidates: List[int], target: int) -> List[List[int]]:
    # Sorting is really helpful, se we can avoid over counting easily
    candidates.sort()
    result = []
    self.combine_sum_2(candidates, 0, [], result, target)
    return result


def combine_sum_2(self, nums, start, path, result, target):
    # Base case: if the sum of the path satisfies the target, we will consider
    # it as a solution, and stop there
    if not target:
        result.append(path)
        return

    for i in range(start, len(nums)):
        # Very important here! We don't use `i > 0` because we always want
        # to count the first element in this recursive step even if it is the same
        # as one before. To avoid overcounting, we just ignore the duplicates
        # after the first element.
        if i > start and nums[i] == nums[i - 1]:
            continue

        # If the current element is bigger than the assigned target, there is
        # no need to keep searching, since all the numbers are positive
        if nums[i] > target:
            break

        # We change the start to `i + 1` because one element only could
        # be used once
        self.combine_sum_2(nums, i + 1, path + [nums[i]], result, target - nums[i])
