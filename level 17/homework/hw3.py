def abbrev_name(name):
    words = name.split()

    first = words[0][0].upper()
    second = words[1][0].upper()

    return first + "." + second