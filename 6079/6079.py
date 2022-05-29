def solution(sentence: str, discount: int) -> str:
    words = sentence.split(" ")
    for i in range(len(words)):
        if len(words[i]) > 1 and words[i][0] == "$":
            if words[i][1:].isdigit():
                d = str(float(words[i][1:])-((float(words[i][1:])*(discount*0.01))))
                print(d)
                if d[::-1].index(".") > 2:
                    # d = d[:d.index(".")+3]
                    d = float(d)
                    d = str(round(d, 2))
                if d[::-1].index(".") < 2:
                    d += "0"

                words[i] = f"${d}"

    return " ".join(word for word in words)

print(solution(sentence = "there are $1 $2 and 5$ candies in the shop", discount = 50))
print(solution(sentence = "sentence = 1 2 $3 4 $5 $6 7 8$ $9 $10$", discount = 100))
print(solution(sentence = "tc7fr$$roqdozd0 $1391", discount = 69))
print(solution(sentence = "l3t0mbk67pj$wo$z456mi5q5ag$zu $857830 $54827203 $8", discount = 84))