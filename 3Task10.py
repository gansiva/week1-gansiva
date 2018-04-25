def has_no_e(word):
    for letter in word:
        if letter=='e':
            return False
    return True
def has_no_e_1():
    fin=open('words.txt')
    i=0
    j=0
    for line in fin:
        word=line.strip()
        result=has_no_e(word)
        if(result==True):
            print(word)
            j=j+1
        i=i+1
    print("Precentage of words in the list that have no 'e' is : ", (j/i)*100)
has_no_e_1()