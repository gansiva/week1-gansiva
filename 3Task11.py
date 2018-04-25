def fn_avoids(word,stri):
    for letter in word:
        if letter in stri:
            return False
    return True
def fn_no_of_words(forbidden):
    fin=open('words.txt')
    for line in fin:
        word=line.strip()
        result=fn_avoids(word,forbidden)
        if(result==True):
            print(word)

forbidden=input("Enter the string of forbidden letters:")
fn_no_of_words(forbidden)