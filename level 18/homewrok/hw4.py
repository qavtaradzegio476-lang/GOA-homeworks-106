def to_jaden_case(string):
    words = string.split()
    
    result = []
    
    for word in words:
        result.append(word[0].upper() + word[1:])
    
    return " ".join(result)