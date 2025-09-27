import random

word_list=["apple","avacado","banana","peach","laptop","harry","computer"]

# random choose a word from the list and assign it to a variable called choosen word
choosen_word=random.choice(word_list)
# print(choosen_word)

# making a blank string for guessing
length=len(choosen_word)
placeholder="_"*length

# for i in range(length):
#     placeholder+="_"
print(placeholder )

print("BEGIN  ")
# Ask use to guess letter of the word assingn it to variable guess and in lowercase
# guess=input("Guess letter of the word : ").lower( )
# print(guess)

# check if the letter exist in the choosen word 
# if guess in choosen_word:
#     print("yes")

correct_letter=[]
lives=5
while lives > 0:
    print("lives ", lives)
    guess=input("Guess letter of the word : ").lower()
    display=""
    for letter in choosen_word:
        if guess==letter:
            display+=letter 
            correct_letter.append(letter)
        elif letter in correct_letter:
            display+=letter
        else: 
            display+="_"
    print(display)

    if display==placeholder:
        lives-=1
    else:
        placeholder=display
    if placeholder==choosen_word:
        print("🎉 WON! The word was:", choosen_word)
        break
 
# print(placeholder)
if lives ==0:
    print("💀 Lost! The word was:", choosen_word)
