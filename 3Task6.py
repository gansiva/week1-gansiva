def add_ing(word):
    if(len(word)<3):
        i=1
        return word,i
    elif(word.find('ing',len(word)-3)==len(word)-3):
        i=2
        word=word+'ly'
        return word,i
    else:
        i=3
        word=word+'ing'
        return word,i
word=input("Enter the string:")
a,b=add_ing(word)
if(b==1):
    print("The given string"," ' ",a," ' ", "length is less than 3")
elif(b==2):
    print("The modified string is "+ a)
elif(b==3):
    print("The modified string is "+ a)
