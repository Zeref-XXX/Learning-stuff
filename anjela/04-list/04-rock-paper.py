import random

option=["rock","paper","se"]
comp=random.choice(option)

user=input("Choose you option : ").lower()
print(f"comp choosed {comp}")


if(user==comp):
    print("Draw")
elif( user=="rock" and comp=="se") or \
   (user=="paper" and comp=="rock") or \
    (user=="se" and comp=="paper") :
    print("user won")
else:
    print("user lost")