class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = []
        d = []
        n = len(senate)
        for i in range(n):
            if senate[i] == "R":
                r.append(i)
            else:
                d.append(i)



        while r and d:
            if r[0] < d[0]:
                d.pop(0)
                r.pop(0)
                r.append(n)
            else:
                r.pop(0)
                d.pop(0)
                d.append(n)

            n += 1

        if r:
            return "Radiant"
        else:
            return "Dire"