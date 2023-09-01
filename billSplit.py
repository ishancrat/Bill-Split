import numpy as np

nameStr=input("Enter names (space separated): ")
print("--------------------------------------------")
names=[i for i in nameStr.split()]
numPpl=len(names)
score=np.zeros((1,numPpl))
while(True):
    for i in range(numPpl):
        print("[",i,"] ",names[i],end="   ")
    expense=int(input("enter total expense for item: "))
    temp=[]
    temp=[int(i) for i in input("space separated ID of payers: ").split()]
     
    if (len(temp)>1):
        tempPaid=[]
        tempPaid=[int(i) for i in input("amt paid by the above respectively: ").split()]

    
    for i in range(len(temp)):
        const=temp[i]
        if (len(temp)==1):
            score[0][const]+=expense
        else:
            const=temp[i]
            score[0][const]+=tempPaid[i]
        
    usedByAll=input("was the commodity used by all?: ")
    equallySplit=input("was the expense equally split?: ")
    
    if (usedByAll=="y"):
        if (equallySplit=="y"):
            perHead=expense/numPpl
            for i in range(numPpl):
                score[0][i]-=perHead
        else:
            personWiseExpense=[]
            personWiseExpense=[int(i) for i in input("person-wise expense in order of ID: ").split()]
                
            for i in range(numPpl):
                score[0][i]-=personWiseExpense[i]
    else:
        if (equallySplit=="y"):
            userID=[]
            userID=[int(i) for i in input("enter ID of consumers (space separated): ").split()]
                
            for i in range(len(userID)):
                temp=userID[i]
                score[0][temp]-=expense/(len(userID))
        else:

            userID=[]
            userID=[int(i) for i in input("enter ID of consumers (space separated): ").split()]
            
            userExpense=[]
            userExpense=[int(i) for i in input("enter amt respectively consumed (space separated): ").split()]
            
            for i in range(len(userID)):
                temp=userID[i]
                score[0][temp]-=userExpense[i]
    flag=input("more expenses?: ")
    if (flag=="y"):
        print()
        continue
    else:
        break

print()        
print("-------------------------------------------------")
print()
print("------------NET BALANCE----------------")
for i in range(numPpl):
    print(i,end="  ")
    print(names[i],end="   ")
    print(score[0][i])
print()
print("-----------------VERDICT---------------")
print()


ID=[int(i) for i in range(numPpl)]

for i in range(numPpl):
    for j in range(numPpl-i-1):
        if (score[0][j]>score[0][j+1]):
            score[0][j],score[0][j+1]=score[0][j+1],score[0][j]
            ID[j],ID[j+1]=ID[j+1],ID[j]

            
index=0
negArr=[]
posArr=[]
IDneg=[]
IDpos=[]

for i in range(numPpl):
    if (score[0][i]<0):
        negArr.append(score[0][i])
        IDneg.append(ID[i])

    else:
        posArr.append(score[0][i])
        IDpos.append(ID[i])
     
        

j=0
i=0 

while(True):
    if i==len(posArr):
        break
    if j==len(negArr):
        break
    
    if (abs(negArr[j])<posArr[i]):
        amt=abs(negArr[j])
        negArr[j]=0
        posArr[i]-=amt
        if (amt!=0):
            print(amt," paid by ",names[IDneg[j]]," to ",names[IDpos[i]])
        j+=1
        i-=1
    elif (abs(negArr[j])==posArr[i]):
        amt=abs(negArr[j])
        negArr[j]=0
        posArr[i]-=amt
        if (amt!=0):
            print(amt," paid by ",names[IDneg[j]]," to ",names[IDpos[i]])
        j+=1
        i+=1
    else:
        amt=posArr[i]
        posArr[i]=0
        if (amt!=0):
            print(amt," paid by ",names[IDneg[j]]," to ",names[IDpos[i]])
        negArr[j]+=amt
        i+=1          
