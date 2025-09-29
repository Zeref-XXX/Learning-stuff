def calculate_love_score(name1,name2):
    item1="true"
    item2="love"
    count1=0
    count2=0
    for char in name1:
        if char.lower()  in item1:
            count1+=1
        if char.lower()  in item2:
            count1+=1   
    

    for char   in name2:
        if char.lower()  in item1:
            count2+=1
        if char.lower()  in item2:
            count2+=1

    print(f"{count1} {count2}")
    
calculate_love_score("Kanye West", "Kim Kardashian")