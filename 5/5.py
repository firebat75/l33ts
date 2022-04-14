def solution(s):

    res = ""
    for i in range(len(s)):
        # odd case, like "aba"
        tmp = helper(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        # even case, like "abba"
        tmp = helper(s, i, i + 1)
        if len(tmp) > len(res):
            res = tmp
    return res


# get the longest palindrome, l, r are the middle indexes
# from inner to outer
def helper(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l + 1 : r]

    # ls = list(s)
    # lsr = ls.copy()
    # lsr.reverse()
    # largest = [s[0]]

    # for x in range(len(ls)):
    #     lsr2 = lsr.copy()
    #     ri = 0
    #     checked = False
    #     while not checked:
    #         print(lsr2)
    #         y = lsr2.index(ls[x])
    #         ri += y + 1
    #         lsr2 = lsr2[y + 1 :]
    #         print(ri)
    #         print(lsr2)
    #         y2 = (y * -1) - 1
    #         print(ls[x], x, y2, ls)
    #         print(ls[x : y2 + 1])
    #         if len(ls) + y2 == x:
    #             checked = True
    #         else:
    #             if y2 == -1:
    #                 temp = ls[x:]
    #             else:
    #                 temp = ls[x : y2 + 1]
    #             print("temp: " + str(temp))

    #             temp2 = temp.copy()
    #             temp2.reverse()
    #             if temp == temp2 and len(temp) > len(largest):
    #                 largest = temp
    # return largest

    # for item in st:
    #     foundlargest = False
    #     temp = ls.copy()
    #     fst = ls.index(item)
    #     ind = 0

    #     while not foundlargest:

    #         tempr = temp.copy()
    #         tempr.reverse()
    #         x = temp.index(item)
    #         y = (tempr.index(item) * -1) - 1

    #         print(item, x, y, temp, tempr, largest)

    #         if y == -1:
    #             temp = temp[x:]
    #         else:
    #             temp = temp[x : y + 1]

    #         print("temp" + str(temp))

    #         if len(temp) <= 1:
    #             try:
    #                 t = ls[fst + 1 :].index(item)
    #                 print(ls, fst, ls[fst + 1 :])
    #                 print(t, ls[fst + 1 :].index(item))
    #                 fst += t + 1
    #                 print("new fst:" + str(fst))
    #                 print("new temp:" + str(temp))
    #                 temp = ls[fst:]
    #             except (ValueError, IndexError):
    #                 print("FOUND LARGEST")
    #                 foundlargest = True

    #         else:
    #             temprev = temp.copy()
    #             temprev.reverse()
    #             if temp == temprev and len(temp) > len(largest):
    #                 largest = temp

    #                 fst += ls[fst + 1 :].index(item) + 1

    #                 try:
    #                     t2 = ls[fst + 1 :].index(item)
    #                     temp = ls[fst:]
    #                     print(temp)
    #                 except (IndexError, ValueError):
    #                     print("ERROR")
    #                     foundlargest = True

    #             temp = temp[:-1]

    # return "".join(largest)

    #     x = ls.index(item)
    #     y = -1
    #     i = x
    #     curr = []
    #     while x != y:
    #         print(item, x, y, i, largest)
    #         try:
    #             y = ls[i + 1 :].index(item) + i + 1
    #             i = y
    #         except (ValueError, IndexError):
    #             y = x

    #         if (y + 1) - x > len(largest):
    #             curr = ls[x : y + 1]
    #             rev = curr.copy()
    #             rev.reverse()
    #             print(curr, rev)
    #             if curr == rev:
    #                 largest = curr

    # return "".join(largest)


# print(solution("babad"))
# print(solution("cbbd"))
# print(solution("ccc"))
# print(solution("aacabdkacaa"))
print(solution("babadada"))
