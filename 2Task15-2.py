def is_palindrome(word):
    """Palindrome check function"""
    j=len(word)-1
    i=0
    while i<j:
        if(word[i]==word[j]):
            i=i+1
            j=j-1
        else:
            return False
        return True
word=input("Enter the string: ")
print("The string to be a palindrome is ",is_palindrome(word))

