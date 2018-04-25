def fn_check(word):
    """"Consecutive double letter check"""
    i=0
    count=0
    while i<len(word)-1:
        if word[i]==word[i+1]:
            count=count+1
            i=i+2
        else:
            i=i+1
    return count
word=input("Enter the word:")
print("Number of times consecutive double letters in the given word",word,"is",fn_check(word))