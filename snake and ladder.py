import random as rdm
ladder=((2,38),(4,14),(8,30),(21,42),(28,76),(50,67),(71,92),(80,99))
snake=((32,10),(36,6),(48,26),(62,18),(88,24),(95,56),(97,78))
p1,p2=input("what are  your names:").split(",")


def turn():
    
    pos1=0
    pos2=0
    n=0
    while(1):
        c=rdm.randint(1,6)
        if(n%2==0):
            
            print("it's your turn",p1,"your position is",pos1)
            pos1+=c
            print(c)
            if(pos1>100):
                print("100 crossed")
                pos1-=c
            pos1=play1(pos1)
        elif(n%2!=0):
            print("it's your turn",p2,"your position is",pos2)
            pos2+=c
            if(pos2>100):
                print("100 crossed")
                pos2-=c
            pos2=play2(pos2)
        
        
        n+=1
        
        if(pos1==100):
            print("yeah p1 wins")
            break
        elif(pos2==100):
            print("yeah p2 wins")
            break


def play1(pos1):
    
    for i in ladder:
        if(i[0]==pos1):
                print("yeah so it's a ladder")
                pos1=i[1]
                break
    else:
        for j in snake:
            if(j[0]==pos1):
                print("yeah so it's a snake")
                pos1=j[1]
                break
    return pos1
        
def play2(pos2):
     for i in ladder:
        if(i[0]==pos2):
                print("yeah so it's a ladder")
                pos2=i[1]
                break
            
     else: 
        for j in snake:
            if(j[0]==pos2):
                print("yeah so it's a snake")
                pos2=j[1]
                break
     return pos2
        
turn()         


    
