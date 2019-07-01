import re
def phoneNumberValidator(phone):
    pattern="^[6-9][0-9]{9}$"
    if re.match(pattern,str(phone)):
        return True
    else:
        return False
def emailValidator(email):
    pattern="^[0-9a-z][0-9a-z_.]{4,14}[@][a-z]{2,13}[.][a-z]{1,4}"
    if re.match(pattern,email):
        return True
    
    return False

def gernerateMarks(n,lb,ub):
    with open("DataFiles/data.txt","w") as f:
        for i in range(0,n):
            r=randint(lb,ub)
            f.write(str(r)+"\n")
            #print(i)
    return
from random import randint

def AverageOfMarks(filepath):
    
    with open(filepath,"r") as f:
        s=f.read().split()
    
        data=[]
    #su=0
        for i in s:
            data.append(int(i))
        s=0
        for i in range(0,len(data)):
            s+=data[i]
        return ("Averg of",s/len(data))
filepath="DataFiles/marks.txt"
def PassPercentage(filepath):
    
    
    with open(filepath,"r") as f:
        s=f.read()
        count=0
        n=10000
        for i in s.split():
            if int(i) > 35:
            
                count=count+1
        return ("Pass Percentage",(count/n)*100)      
filepath="DataFiles/marks.txt"
def FailPercentage(filepath):
    with open(filepath,"r") as data:
        s=data.read()
        count=0
        n=10000
        for i in s.split():
            if int(i)<=35:
                count+=1
        return ("Fail Percentage",(count/n)*100)
filepath="DataFiles/marks.txt"
def DistentionPercentage(filepath):
    with open(filepath,"r") as data:
        s=data.read()
        count=0ss
        n=10000
        for i in s.split():
            if int(i)>=70:
                count+=1
        return ("Distention of",(count/n)*100)
filepath="DataFiles/marks.txt"

def allFunctionsinSingleFun(filepath):
    
    AverageOfMarks(filepath)
    PassPercentage(filepath)
    FailPercentage(filepath)
    DistentionPercentage(filepath)
    highestNLowestFrequency(filepath)
    
filepath="DataFiles/data.txt"  