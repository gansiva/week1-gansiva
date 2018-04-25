def is_abecedarian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True
def how_many():
    fin = open('words.txt')
    i = 0
    for line in fin:
        word = line.strip()
        result = is_abecedarian(word)
        if (result == True):
            print(word)
            i = i + 1
    return i

print("No of abecedarian words in the list is",how_many())
