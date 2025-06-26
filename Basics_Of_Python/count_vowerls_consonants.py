def count_vowels_consonants():
    word = input("Enter a string: ")
    vowels ='aeiou'
    vowels_count =0
    consonants_count =0

    for char in word.lower():
        if char.isalpha():
            if char in vowels:
                vowels_count += 1
            else:
                consonants_count += 1
    print(f"Vowels Count is {vowels_count}")
    print(f"Consonants Count is {consonants_count}")


count_vowels_consonants()