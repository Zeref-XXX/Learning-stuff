import random

word_list=["apple","avacado","banana","peach","laptop","harry","computer"]
art=[
    """
    +-------+
    |       |
    O       |
   /|\\     |
   / \\     |
            |
    ========
    """,

    """
    +-------+
    |       |
    O       |
   /|\\     |
   /        |
            |
    ========
    """,

    """
    +-------+
    |       |
    O       |
   /|\\     |
            |
            |
    ========
    """,

    """
    +-------+
    |       |
    O       |
   /|       |
            |
            |
    ========
    """,

    """
    +-------+
    |       |
    O       |
   /        |
            |
            |
    ========
    """    ,

    """
    +-------+
    |       |
            |
            |
            |
            |
    ========
    """,

    """
    +-------+
            |
            |
            |
            |
            |
    ========
    """
] 

choosen_word=random.choice(word_list)
 
length=len(choosen_word)
placeholder="_"*length
  

correct_letter=[]
lives=6
while lives > 0:
    print(art[lives])
    guess=input("Guess letter  : ").lower()
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
        print(" ❤️ "* lives)
    else:
        placeholder=display
    if placeholder==choosen_word:
        print("🎉 WON! The word was:", choosen_word)
        break
 
# print(placeholder)
if lives ==0:
    print("💀 Lost! The word was:", choosen_word)
