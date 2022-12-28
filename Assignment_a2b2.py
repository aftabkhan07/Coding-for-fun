## using nested for
a = "aabbccccdaafff"
c = ""
counter = 0

for i in range(0,len(a)):
    if len(c) == 0:
        c+=a[i]
    elif a[i]!=c[-1] :
        c+=str(counter)
        c+=a[i]
        counter = 0
    elif i == (len(a)-1):
        c+=str(counter)
        break
    elif a[i]==c[-1]:
        continue
    for j in range(i,len(a)):
        if a[i]==a[j]:
            counter+=1
        
print(c)

#a4b2c4d1a2f3



