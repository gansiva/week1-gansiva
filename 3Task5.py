def find_letter(word,letter):
    return word.count(letter)
word=input("Enter the string:")
letter=input("Enter the letter to find in the string:")
print(find_letter(word,letter))
