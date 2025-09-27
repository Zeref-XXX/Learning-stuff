bill=0

size=input("Enter the size of pizza , s, m, or l ").lower()
pepper=input("need pepperoni, y or n ").lower
if size=='s':
    bill+=15
    if pepper=='y':
        bill+=2
    
elif size=="m":
    bill+=20
    if pepper=='y':
        bill+=3
else:
    bill+=25
    if pepper=='y':
        bill+=3

print("you bill is : {}".format(bill))
