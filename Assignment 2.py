num=int(input("enter max ticket available"))
participant=[]
for i in range(0,num):
    x=input("enter name:")
    participant.append(x)
import random
b = random.randint(0,num-1)
print("Participants are: ",participant)
print('Winner is : ',participant[b])
