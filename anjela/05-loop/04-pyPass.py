# Password generator
import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=[1,2,3,4,5,6,7,8,9,0]
symbols=['!','@','#','$','%','^']

# print(type(str(numbers[0])))

# ans=""
# for num in numbers:
#     ans+=str(num)
# print(ans)

print("PassWord generator \n")
n_letters=int(input("ENter the number of letters \n"))
n_symbols=int(input("ENter the number of symbols \n"))
n_numbers=int(input("ENter the number of numbers \n"))

# ----------------------------easy mode 
# PassWord=""
# for i in range(0,n_letters):
#     PassWord+=random.choice(letters)
# for i in range(0,n_symbols):
#     PassWord+=random.choice(symbols)
# for i in range(0,n_numbers):
#     PassWord+=str(random.choice(numbers))

# print(PassWord)

# ----------------------------harrd
PassWord_list=[]
for i in range(0,n_letters):
    PassWord_list.append(random.choice(letters))
for i in range(0,n_symbols):
    PassWord_list+=random.choice(symbols)
for i in range(0,n_numbers):
    PassWord_list+=str(random.choice(numbers))

random.shuffle(PassWord_list)
result=""
for char in PassWord_list:
    result+=char



print(PassWord_list)
print(result)

