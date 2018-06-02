# File: BabyNames.py

#  Description: A program for BabyNames

#  Student's Name: Zongpeng Chen

#  Student's UT EID: zc3543
 
#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E 

#  Unique Number: 51335

#  Date Created:03/19/2018

#  Date Last Modified:03/23/2018

def exist(name,diction):
    list1=list(diction.keys())
    Flag=False
    for i in range(len(list1)):
        if name==list1[i]:
            Flag=True
            break
        else:
            Flag=False
    return Flag           

def display(name,diction):
    if name in diction:
        print()
        print(name+':',end='')
        for i in range(len(diction[name])):
            if diction[name][i]==1001:
                diction[name][i]=0
            print(str(diction[name][i]),end=' ')
        print()
        print('1900: '+str(diction[name][0]))
        print('1910: '+str(diction[name][1]))
        print('1920: '+str(diction[name][2]))
        print('1930: '+str(diction[name][3]))
        print('1940: '+str(diction[name][4]))
        print('1950: '+str(diction[name][5]))
        print('1960: '+str(diction[name][6]))
        print('1970: '+str(diction[name][7]))
        print('1980: '+str(diction[name][8]))
        print('1990: '+str(diction[name][9]))
        print('2000: '+str(diction[name][10]))
    else:
        print(str(name)+' does not appear in any decade')
        
def onlyone(decade,name,diction):
    if name in diction:
        if diction[name].count(1001)==10 and diction[name][int((decade-1900)/10)]!=1001:
            return True

def sortlist(decade,list1,diction):
    list2=[]
    for item in list1:
        list2.append(diction[item][int((decade-1900)/10)])
    list2.sort()
    list3=[]
    for i in range(len(list2)):
        for item in list1:
            if diction[item][int((decade-1900)/10)]==list2[i]:
                   list3.append(item)
    return [list3,list2]
                   
def all(name,diction):
    if name in diction:
        if diction[name].count(1001)==0:
            return True

def morepop(name,diction):
    Flag=False
    if name in diction and all(name,diction):
        for i in range(len(diction[name])-1):
            if diction[name][i]>=diction[name][i+1]:
                Flag=True
                continue
            else:
                Flag=False
                break
    return Flag

def lesspop(name,diction):
    Flag=False
    if name in diction and all(name,diction):
        for i in range(len(diction[name])-1):
            if diction[name][i]<=diction[name][i+1]:
                Flag=True
                continue
            else:
                Flag=False
                break
    return Flag
                
def main():
    Goodbyeflag=False
    name_dict={}
    name=open('names.txt','r',encoding = 'utf8')
    namelist=[]
    for line in name:
        line=line.strip()
        line=line.split()
        name_dict[line[0]]=list(line[1:])
        for i in range(len(name_dict[line[0]])):
            if name_dict[line[0]][i]=='0':
                name_dict[line[0]].remove('0')
                name_dict[line[0]].insert(i,'1001')
            name_dict[line[0]][i]=int(name_dict[line[0]][i])
    print('Options:')
    print('Enter 1 to search for names.')
    print('Enter 2 to display data for one name.')
    print('Enter 3 to all names that appear in only one decade.')
    print('Enter 4 to all names that appear in all decades.')
    print('Enter 5 to all names that are more popular in every decade.')
    print('Enter 6 to all names that are less popular in every decade.')
    print('Enter 7 to quit.')
    print()
    choi=input('Enter choice:')
    try:
        choi=int(choi)
    except ValueError:
        print('Value Error')
    finally:
        while choi==1 or choi==2 or choi==3 or choi==4 or choi==5 or choi==6:
            if choi==1:
                cha=str(input('Enter a name:'))
                if exist(cha,name_dict):
                    print()
                    max1=1001
                    i=0
                    choo=[]
                    while i < len(name_dict[cha]):
                        if name_dict[cha][i]<max1:
                            max1=name_dict[cha][i]
                            choo.append(i)
                            i+=1
                        elif name_dict[cha][i]==max1:
                            choo.append(i)
                            i+=1
                        else:
                            i+=1
                    print('The matches with their highest ranking decade are:')
                    print(str(cha)+' ',end='')
                    print(str(1900+choo[-1]*10),end=' ')
                    print()
                    print('Options:')
                    print('Enter 1 to search for names.')
                    print('Enter 2 to display data for one name.')
                    print('Enter 3 to all names that appear in only one decade.')
                    print('Enter 4 to all names that appear in all decades.')
                    print('Enter 5 to all names that are more popular in every decade.')
                    print('Enter 6 to all names that are less popular in every decade.')
                    print('Enter 7 to quit.')
                    print()
                    choi=input('Enter choice:')
                    try:
                        choi=int(choi)
                    except ValueError:
                        print('Value Error')
                if not exist(cha,name_dict):
                    print(cha+'does not appear in any decade.')
                    print()
                    print()
                    print('Options:')
                    print('Enter 1 to search for names.')
                    print('Enter 2 to display data for one name.')
                    print('Enter 3 to all names that appear in only one decade.')
                    print('Enter 4 to all names that appear in all decades.')
                    print('Enter 5 to all names that are more popular in every decade.')
                    print('Enter 6 to all names that are less popular in every decade.')
                    print('Enter 7 to quit.')
                    print()
                    choi=input('Enter choice:')
                    try:
                        choi=int(choi)
                    except ValueError:
                        print('Value Error')
            if choi==2:
                cha=str(input('Enter a name:'))
                display(cha,name_dict)
                print()
                print()
                print('Options:')
                print('Enter 1 to search for names.')
                print('Enter 2 to display data for one name.')
                print('Enter 3 to all names that appear in only one decade.')
                print('Enter 4 to all names that appear in all decades.')
                print('Enter 5 to all names that are more popular in every decade.')
                print('Enter 6 to all names that are less popular in every decade.')
                print('Enter 7 to quit.')
                print()
                choi=input('Enter choice:')
                try:
                    choi=int(choi)
                except ValueError:
                    print('Value Error')
            if choi==3:
                cha=int(input('Enter a decade:'))
                if cha%10==0:
                    list3=[]
                    list2=[]
                    for item in name_dict.keys():
                        if onlyone(cha,item,name_dict):
                            list3.append(item)
                    print('The name are in order of rank:')
                    list3=sortlist(cha,list3,name_dict)[0]
                    list2=sortlist(cha,list3,name_dict)[1]
                    for i in range(len(list3)):
                        print(str(list3[i])+': '+str(list2[i]))
                else:
                    print('Value Error')
                print()
                print('Options:')
                print('Enter 1 to search for names.')
                print('Enter 2 to display data for one name.')
                print('Enter 3 to all names that appear in only one decade.')
                print('Enter 4 to all names that appear in all decades.')
                print('Enter 5 to all names that are more popular in every decade.')
                print('Enter 6 to all names that are less popular in every decade.')
                print('Enter 7 to quit.')
                print()
                choi=input('Enter choice:')
                try:
                    choi=int(choi)
                except ValueError:
                    print('Value Error')
            if choi==4:
                 list4=[]
                 for item in name_dict.keys():
                     if all(item,name_dict):
                         list4.append(item)
                 print(str(len(list4))+' names appear in every decade. The names are:')
                 for item in list4:
                     print(item)
                 print()
                 print('Options:')
                 print('Enter 1 to search for names.')
                 print('Enter 2 to display data for one name.')
                 print('Enter 3 to all names that appear in only one decade.')
                 print('Enter 4 to all names that appear in all decades.')
                 print('Enter 5 to all names that are more popular in every decade.')
                 print('Enter 6 to all names that are less popular in every decade.')
                 print('Enter 7 to quit.')
                 print()
                 choi=input('Enter choice:')
                 try:
                     choi=int(choi)
                 except ValueError:
                     print('Value Error')
            if choi==5:
                 list5=[]
                 for item in name_dict.keys():
                     if morepop(item,name_dict):
                         list5.append(item)
                 print(str(len(list5))+' names are more popular in every decade.')
                 for item in list5:
                     print(item)
                 print()
                 print('Options:')
                 print('Enter 1 to search for names.')
                 print('Enter 2 to display data for one name.')
                 print('Enter 3 to all names that appear in only one decade.')
                 print('Enter 4 to all names that appear in all decades.')
                 print('Enter 5 to all names that are more popular in every decade.')
                 print('Enter 6 to all names that are less popular in every decade.')
                 print('Enter 7 to quit.')
                 print()
                 choi=input('Enter choice:')
                 try:
                     choi=int(choi)
                 except ValueError:
                     print('Value Error')
            if choi==6:
                 list6=[]
                 for item in name_dict.keys():
                     if lesspop(item,name_dict):
                         list6.append(item)
                 print(str(len(list6))+' names are more popular in every decade.')
                 for item in list6:
                     print(item)
                 print()
                 print('Options:')
                 print('Enter 1 to search for names.')
                 print('Enter 2 to display data for one name.')
                 print('Enter 3 to all names that appear in only one decade.')
                 print('Enter 4 to all names that appear in all decades.')
                 print('Enter 5 to all names that are more popular in every decade.')
                 print('Enter 6 to all names that are less popular in every decade.')
                 print('Enter 7 to quit.')
                 print()
                 choi=input('Enter choice:')
                 try:
                     choi=int(choi)
                 except ValueError:
                     print('Value Error')
            if choi!=1 and choi!=2 and choi!=3 and choi!=4 and choi!=5 and choi!=6:
                print()
                print()
                print('Goodbye.')
                Goodbyeflag=True
                break
        if choi!=1 and choi!=2 and choi!=3 and choi!=4 and choi!=5 and choi!=6 and Goodbyeflag==False:
                print()
                print()
                print('Goodbye.')
    name.close()
main()


