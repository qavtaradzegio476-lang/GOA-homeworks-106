def accum(s):
    result = []

    for i in range(len(s)):
        letter = s[i].upper()
        result.append(letter + s[i].lower() * i)

    return "-".join(result)