import re
a = "a3b5c13"
c = ""

numreg = re.compile(r"[a-z]{1}\d{1,2}")
mo = numreg.findall(a)

for i in mo:
    c += i[0]*int(i[1:]) 

print(c)
    
#aaabbbbbccccccccccccc