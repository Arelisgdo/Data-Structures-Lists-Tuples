def multiple_returns(frase):
    length = len(frase)
    first = None if length == 0 else frase[0]
    return length, first
