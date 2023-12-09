import numpy as np
import pandas as pd
from datetime import datetime 

tripWasToday = input("was the trip scheduled today? : ")
if (tripWasToday.upper() == "Y"):
    date = datetime.now()
    date = date.strftime("%d-%m-%Y")
else:
    date = input("enter trip's date in format DD-MM-YYYY (hyphens included): ")
header = []
header.append(["Expense"])

nameStr=input("Enter names (space separated): ")
print("--------------------------------------------")
names=[i for i in nameStr.split()]

for i in names:
    header[0].append(i)
    
rowPtr = 1

numPpl=len(names)
score=np.zeros((1,numPpl))


while(True):
    templst = []
    temp=[]
    moreThanOnePayer = False
    for i in range(numPpl):
        print("[",i,"] ",names[i],end="   ")
    expenseName = input("Expense Title: ")
    templst.append(expenseName)
    
    expense=int(input("enter total expense for item: "))
    
    temp=[int(i) for i in input("space separated ID of payers: ").split()]
     
    if (len(temp)>1):
        moreThanOnePayer = True
        tempPaid=[]
        tempPaid=[float(i) for i in input("amt paid by the above respectively: ").split()]

    
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
                templst.append(perHead)
                
        else:
            personWiseExpense=[]
            personWiseExpense=[float(i) for i in input("person-wise expense in order of ID: ").split()]
                
            for i in range(numPpl):
                score[0][i]-=personWiseExpense[i]
                templst.append(personWiseExpense[i])
    else:
        if (equallySplit=="y"):
            userID=[]
            userID=[int(i) for i in input("enter ID of consumers (space separated): ").split()]
            numWhoDidNotConsume = len(userID)
            blankLst = [0 for i in range(numPpl)]
            templst = templst + blankLst
            
            for i in range(len(userID)):
                tempp=userID[i]
                score[0][tempp]-=expense/(len(userID))
                templst[userID[i]+1] = (expense/len(userID))
        else:

            userID=[]
            userID=[int(i) for i in input("enter ID of consumers (space separated): ").split()]
            blankLst = [0 for i in range(numPpl)]
            templst = templst + blankLst
            userExpense=[]
            userExpense=[float(i) for i in input("enter amt respectively consumed (space separated): ").split()]
            
            for i in range(len(userID)):
                tempp=userID[i]
                score[0][tempp]-=userExpense[i]
                templst[userID[i]+1] = (userExpense[i])
                
    if (moreThanOnePayer):
        for i in range(len(temp)):
            templst.append(tempPaid[i])
            templst.append(names[temp[i]])
    else:
        templst.append(expense)
        templst.append(names[temp[0]])
        
    header.append(templst)
    flag=input("more expenses?: ")
    if (flag=="y"):
        print()
        continue
    else:
        break

header.append([])     
print()        
print("-------------------------------------------------")
print()
print("------------NET BALANCE----------------")
for i in range(numPpl):
    temp=[]
    print(i,end="  ")
    print(names[i],end="   ")
    temp.append(names[i])
    print(score[0][i])
    temp.append(score[0][i])
    header.append(temp)
print()
print("-----------------VERDICT---------------")
print()

header.append([])

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
    temp=[]
    
    
    if (abs(negArr[j])<posArr[i]):
        amt=abs(negArr[j])
        negArr[j]=0
        posArr[i]-=amt
        if (amt!=0):
            print(amt," paid by ",names[IDneg[j]]," to ",names[IDpos[i]])
            temp.append(names[IDneg[j]])
            temp.append("to")
            temp.append(names[IDpos[i]])
            temp.append(amt)
        header.append(temp)  
        j+=1
#         i-=1
    elif (abs(negArr[j])==posArr[i]):
        amt=abs(negArr[j])
        negArr[j]=0
        posArr[i]-=amt
        if (amt!=0):
            print(amt," paid by ",names[IDneg[j]]," to ",names[IDpos[i]])
            temp.append(names[IDneg[j]])
            temp.append("to")
            temp.append(names[IDpos[i]])
            temp.append(amt)
        header.append(temp)
        j+=1
        i+=1
    else:
        amt=posArr[i]
        posArr[i]=0
        if (amt!=0):
            print(amt," paid by ",names[IDneg[j]]," to ",names[IDpos[i]])
            temp.append(names[IDneg[j]])
            temp.append("to")
            temp.append(names[IDpos[i]])
            temp.append(amt)
        header.append(temp)
        negArr[j]+=amt
        i+=1
        
