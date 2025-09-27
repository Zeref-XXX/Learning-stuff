print("Welcome to tresure island : Find the tresure ")

side=input("which side to move l or r ").lower()
swim=input("swim or wait ").lower()
door=input("choose door blue  red or yellow ").lower()

if side=='l' and swim=='wait':
    if door=='yellow':
        print("You win ")
else:
    print("You lost")
