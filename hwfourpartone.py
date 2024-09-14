print('Welcome to palindrome checker!')
def is_palindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]

user_input = input("Enter the word you want to check: ")


if is_palindrome(user_input):
    print("It is a palindrome")
else:
    print("It is NOT a palindrome.")
