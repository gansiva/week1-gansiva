def is_palindrome(word):
    i=0
    j=len(word)-1
    while i<=j:
        if(word[i]!=word[j]):
            return False
        else:
            i=i+1
            j=j-1
    return True
word=input("Enter the palindrome:")
print("The entered string to be a palindrome is ",is_palindrome(word))


