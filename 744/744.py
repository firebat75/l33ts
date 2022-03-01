def nextGreatestLetter(letters: list[str], target: str) -> str:
    for letter in letters:
        if ord(target) < ord(letter):
            return letter

    return letters[0]
