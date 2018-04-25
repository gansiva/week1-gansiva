def uses_all(word,stri):
    for letter in word:
        if letter not in stri:
            return False
    return True

def fn_no_of_words(stri):
    fin=open('words.txt')
    i=0
    for line in fin:
        word=line.strip()
        result=uses_all(word,stri)
        if(result==True):
            print(word)
            i=i+1
    return i

stri=input("Enter the string of letters:")
print("No of words in the list with",stri,"is",fn_no_of_words(stri))

