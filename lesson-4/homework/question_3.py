txt = input("Enter the string: ")
yangisi = ""
harf = ["a", "e", "u", "i", "o"]
i = 0
count = 0
while i<(len(txt) - 1):
    yangisi += txt[i]
    count+=1
    if count >= 3:
        if txt[i] not in harf:
            yangisi+="_"
            harf.append(txt[i])
            count = 0
        
    i+=1
yangisi+=txt[-1]

print(yangisi)