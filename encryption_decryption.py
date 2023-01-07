def encode(string):
    list1 = string.split(" ")
    list2 = []
    import random
    import string

    randstr = ''.join(random.choices(string.ascii_lowercase, k=6))

    for i in list1:
        string1 = ""
        if len(i) < 3 :
            string1+=i[::-1]
        else:
            string1=i[1:]
            string1+=i[0]
            string1= string1[::-1]
            string1 = f"{randstr[:3]}{string1}{randstr[3:]}"
        list2.append(string1)
    return list2


def decode(string):
    list1 = string.split(" ")
    list2 = []

    for i in list1:
        string1 = ""
        if len(i) < 3 :
            string1+=i[::-1] 
        else:
            string1+=i[3:-3] # gldabatfrsa
            string1=string1[::-1]
            string1 = f"{string1[-1]}{string1}"
            string1 = string1[:-1]
            
        list2.append(string1)
    return list2

while True:
    input1 = input("If u want to encode please press 'e' else press 'd' for decode and enter  : ")
    input2 = input("Enter the string : ")

    if input1 == "e" :
        result = encode(input2)
        eresult = " ".join(result)
        print(f"your encoded string is \"{eresult}\"")
    elif input1 == "d":
        result = decode(input2)
        eresult = " ".join(result)
        print(f"your decoded string is \"{eresult}\"")
    eresult = " ".join(result)


    print("----------------------------------------")