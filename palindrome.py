def palindrome():
    word = input("Enter a Word: ")
    reversed_word=""
    for char in word:
        reversed_word= char + reversed_word
    if reversed_word == word:
            print(f"{word} is palindrome")
    else:
         print(f"{word} is not palindrome")


palindrome()
        
