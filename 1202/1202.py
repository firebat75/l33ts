def solution(s, pairs):
    print(pairs)
    d = {}
    for a, b in pairs:
        if a not in d:
            d[a] = [b]
        else:
            d[a].append(b)
        
        if b not in d:
            d[b] = [a]
        else:
            d[b].append(a)

    print(d)
    def dfs(x,A):
        print(f"in dfs - x: {x}, A: {A}")
        if x in d:
            A.append(x)
            for y in d.pop(x):
                dfs(y,A)
    #
    s    = list(s)
    while d:
        x = next(iter(d))
        A = []
        print(f"pre dfs - x: {x}, A: {A}")
        dfs(x,A)
        A = sorted(A)
        B = sorted([ s[i] for i in A ])
        print(f"A: {A}, B: {B}, d: {d}")
        for i,b in enumerate(B):
            s[A[i]] = b
            print(''.join(s))
    return ''.join(s)

# print(solution("dcab", [[0,3], [1,2]]))
print(solution("dcab", [[0,3], [1,2], [0,2]]))
# print(solution("cba", [[0,1], [1,2]]))