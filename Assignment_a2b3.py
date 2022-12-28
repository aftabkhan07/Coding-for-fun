## using single for loop
a = "aabbccccdaafff"
c = ""
counter = 1

for i in range(len(a)):
    if len(c)==0:
        c+=a[i]
    elif c[-1]!=a[i]:
        c+=str(counter)
        c+=a[i]
        counter = 1
    elif i == (len(a)-1):
        c+=str(counter+1)
    elif c[-1]==a[i]:
        counter+=1
        
print(c)

#a2b2c4d1a2f3




