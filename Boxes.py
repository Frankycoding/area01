# File: Boxes.py

#  Description: A program for Boxes

#  Student's Name: Zongpeng Chen

#  Student's UT EID: zc3543
 
#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E 

#  Unique Number: 51335

#  Date Created:02/16/2018

#  Date Last Modified:02/22/2018

def savenum(c):
    list1=[]
    a=len(c)
    for i in range(a):
        if c[i].isdigit() and c[i+1].isdigit():
            list1.append(int(c[i])*10+int(c[i+1]))
    return list1
        
def is_subset(c,d):
    for i in range(3):
        if c[i]<d[i]:
            continue
        else:
            return False
    return True

def subset(a,b,to,lo,blist):
    hi=len(to)
    if lo==hi:
        d=b[:]
        blist.append(d)
        return blist
    else:
        c=[]
        Flag=False
        for i in range(hi):
            if is_subset(a,to[i]):
                c.append(to[i])
                Flag=True
        if Flag==True:
            len1=len(c)
            for i in range(len1):
                b.append(c[i])
                subset(c[i],b,to,lo+1,blist)
                b.remove(c[i])
        else:
            subset(a,b,to,lo+1,blist)
 
def main():
    filevar=open('boxes.txt','r')
    num=int(filevar.readline())
    list2=[]
    for i in range(num):
        p=filevar.readline()
        p=savenum(p)
        list2.append(p)
    Sortedlist2=[]
    for i in range(num):
        Sortedlist2.append(sorted(list2[i]))
    Sortedlist2.sort()
    to=Sortedlist2
    bllist=[]
    for i in range(num):
        blist=[]
        b=[to[i]]
        subset(to[i],b,to,0,blist)
        bllist.append(blist)
    op=[]
    lenmax=len(bllist[0][0])
    for i in range(num):
        for j in range(len(bllist[i])):
            if len(bllist[i][j])>lenmax:
                lenmax=len(bllist[i][j])
    for i in range(num):
        for j in range(len(bllist[i])):
            if len(bllist[i][j])==lenmax:
                op.append(bllist[i][j])
    if lenmax>1:
        print('Largest Subset of Nesting Boxes')
        for i in range(len(op)):
            for j in range(lenmax):
                print(op[i][j])
            print()
    else:
        print('No Nesting Boxes')
main()
        
    
