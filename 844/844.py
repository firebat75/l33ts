def backspaceCompare(s, t):
    stacks = 0
    stackt = 0
    s2 = ""
    t2 = ""
    # for i in range(-1, len(max(s, t)) * -1, -1):
    while len(s) > 0:
        if s[-1] == "#":
            stacks += 1
        else:
            if stacks == 0:
                s2 += s[-1]
            else:
                stacks -= 1
        s = s[:-1]

    while len(t) > 0:

        if t[-1] == "#":
            stackt += 1
        else:
            if stackt == 0:
                t2 += t[-1]
            else:
                stackt -= 1
        t = t[:-1]

    print("s", s, s2, stacks)
    print("t", t, t2, stackt, "\n")

    return s2 == t2


x = backspaceCompare("ab#c", "ad#c")
y = backspaceCompare("ab##", "c#d#")
z = backspaceCompare("a#c", "b")

a = backspaceCompare("xywrrmp", "xywrrmu#p")
