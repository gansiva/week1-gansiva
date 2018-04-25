def rotate_word(word,num):
    i=0
    nword=" "
    for i in range(len(word)):
        a=ord(word[i])
        if((num+a)<97): #a-z reference created
            n=97-(num+a)
            b=chr(123-n)
        elif((num+a)>122): #a-z reference created
            n=(num+a)-122
            b=chr(96+n)
        else:
            b=chr(num+a)
        nword=nword+b
    return nword
word=input("Enter the string:")
num=int(input("Enter the number of times to rotate the string literal:"))
print("Encoded output is:",rotate_word(word,num))