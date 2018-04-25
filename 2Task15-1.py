def first(word):
    """Prints first letter in the word"""
    return word[0]

def last(word):
    """Prints last letter in the word"""
    return word[-1]

def middle(word):
    """Prints middle letter based on the indices"""
    return word[1:-1]

print(middle("ly"))
print(first("l"))
print(middle(" "))
print(middle("elephant"))
print(last("elephant"))