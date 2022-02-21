# Write a python program to ask for the word, and check if the word is palindrome, length of the word, reverse the word.


string = input("Enter the string")

rev_str=(string[::-1])
print(rev_str)

if rev_str==string:
    print("palindrome")
else:
    print("Not Palindrome")
    print(len(string))
