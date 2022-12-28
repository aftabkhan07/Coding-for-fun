import random
from kbcdata import qna

winning = 0
chances = 0
randqna = []
    
for i in range(len(qna)):
    n = random.choice(qna)
    qna.remove(n)
    randqna.append(n)
			
for i in randqna:
    print(i["question"])
    for j in i["options"]:
        print(f'''- {j["option"]}''')
    ans = input("please enter your answer: ").lower()
    if ans == i["answer"].lower():
        print("correct!!!\n")
        if chances == 0:
            winning += 1000
        else:
            winning = winning*2
            chances += 1
    else:
        print("You lost")
        print(f'Answer was {i["answer"]}')
        break

print ("Thanx for playing!!!")
print (f"you won {winning}")     
    
    
    
    
    
    