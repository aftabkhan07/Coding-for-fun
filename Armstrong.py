# Armstrong number

a = input("Please enter the input: ")
Armstrong = []

for i in range(int(a)):
    b = []
    for j in range(len(str(i))):
        b.append(int(str(i)[j])**len(str(i)))

    if sum(b)==int(i):
        Armstrong.append(i)

print(Armstrong)