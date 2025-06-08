def minion_game(string):
    vowels = set('AEIOU')
    kevin_score = 0
    stuart_score = 0
    n = len(string)

    for i, ch in enumerate(s):
        if ch in vowels:
            kevin_score += n - i
        else:
            stuart_score += n - i

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")


if __name__ == '__main__':