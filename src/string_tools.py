
def split(word):
    return [str(char) for char in word]

def join(words):
    r = ""
    for w in words:
        r += w

    return r

def repeat(string, how_many_times):
    result = ""
    for i in range(how_many_times):
        result += string
    return result