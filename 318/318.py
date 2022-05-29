def solution(words: list[str]) -> int:
        output = 0

        if len(words) == 1:
            return 0

        i = 1

        temp = words[i:].copy()

        for word in words:
            temp = words[i:].copy()
            for word2 in temp:
                if word[0] not in word2:
                    comp = True
                    for letter in word:
                        if letter in word2:
                            comp = False

                    if comp:
                        output = max(len(word)*len(word2), output)
                    
            i += 1

        return output


print(solution(words = ["abcw","baz","foo","bar","xtfn","abcdef"]))