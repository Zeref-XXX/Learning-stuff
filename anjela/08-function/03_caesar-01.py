# part1 caesar 
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encode(text,shift):    
    ans=""
    for char in text: 
        if char not in alphabet:
            ans+=char
            continue
        index=alphabet.index(char)
        ans+=alphabet[(index+shift)%len(alphabet)]

    print(ans)

def decode(text,shift):    
    ans=""
    for char in text: 
        if char not in alphabet:
            ans+=char
            continue
        index=alphabet.index(char)
        # newInd=index-shift
        # if newInd <0:
        #     newInd=26+newInd
        newInd = (index - shift) % len(alphabet)
        ans+=alphabet[newInd%26]

    print(ans)

choice=input(" Encode or decode ")

text=input("Type the text for encodding ")
shift=int(input("Type the shift amount "))


match choice:
    case "encode":
        print("encoding ")
        encode(text,shift)
         
    case "decode":
        print("decoding  ")
        decode(text,shift)
    case _:
        print("INVALID")         
