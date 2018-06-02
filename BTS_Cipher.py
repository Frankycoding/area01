#  File: BST_Cipher.py

#  Description: A program for BST_Cipher

#  Student Name:Zongpeng Chen

#  Student UT EID:zc3543

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created:04/12/2018

#  Date Last Modified:04/18/2018

def encrypt2 (st):
    str1=''
    hm=list(st)
    hm2=[]
    for item in hm:
      if item.isalpha():
        text=item.lower()
        hm2.append(text)
      if item==' ':
        hm2.append(item)
    for item in hm2:
      str1+=item
    return str1

class Node (object):
    def __init__ (self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class Tree (object):
  # the init() function creates the binary search tree with the
  # encryption string. If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character drop that character.
  def __init__ (self, encrypt_str):
    self.root=None
    self.data=self.encrypt1(encrypt_str)
    self.nr=[]
    for item in self.data:
        self.insert(item)  

  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
  def insert (self, ch):
    if self.nr.count(ch)==0:
        self.nr.append(ch)
        new_node = Node (ch)
        index=ord(ch)
        if (self.root == None):
          self.root = new_node
        else:
          current = self.root
          parent = self.root
          while (current != None):
            parent = current
            if (index < ord(current.data)):
                current = current.lchild
            else:
                current = current.rchild
          if (index < ord(parent.data)):
            parent.lchild = new_node
          else:
            parent.rchild = new_node  

  # the search() function will search for a character in the binary
  # search tree and return a string containing a series of lefts
  # (<) and rights (>) needed to reach that character. It will
  # return a blank string if the character does not exist in the tree.
  # It will return * if the character is the root of the tree.
  def search (self, ch):
    str1=''
    index=ord(ch)
    current = self.root
    if ch==current.data:
      return '*'
    while (current != None) and (current.data != chr(index)):
      if (index < ord(current.data)):
        str1+='<'
        current = current.lchild
      else:
        current = current.rchild
        str1+='>'
    if current==None:
        return ''
    else:
        return str1

  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding 
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.
  def traverse (self, st):
    comm=list(st)
    current=self.root
    if len(comm)==0:
        return '  '
    if len(comm)==1:
      if comm[0]=='*':
        return current.data
      if comm[0]=='<':
        if current.lchild==None:
            return '  '
        else:
            return current.lchild.data
      if comm[0]=='>':
        if current.rchild==None:
            return '  '
        else:
            return current.rchild.data
      else:
        return '  '
    else:
        len1=len(comm)
        i=0
        while current!=None and i<len1:
          if comm[i]=='<':
            current=current.lchild
            i+=1
          else:
            current=current.rchild
            i+=1
        if current==None:
            return '  '
        else:
            return current.data
        
  def encrypt1 (self, st):
    str1=''
    hm=list(st)
    hm2=[]
    for item in hm:
      if item.isalpha():
        text=item.lower()
        hm2.append(text)
      if item==' ':
        hm2.append(item)
    for item in hm2:
      str1+=item
    return str1

  # the encrypt() function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
  def encrypt(self,st):
    str1=''
    list1=list(st)
    for i in range(len(list1)-1):
      a=self.search(list1[i])
      str1+=a
      str1+='!'
    str1+=self.search(list1[-1])
    return str1
         
  # the decrypt() function will take a string as input parameter, and
  # return the decrypted string.
  def decrypt (self, st):
    str1=''
    hm=st.split('!')
    for item in hm:
        a=self.traverse(item)
        if a=='  ':
            return 'N'
            break
        else:
            str1+=a
    return str1

def main():
  print()
  text=input('Enter encryption key: ')
  tree=Tree(text)
  print()
  text2=input('Enter string to be encrypted:')
  text2=encrypt2(text2)
  print('Encrpted string: ',end='')
  print(tree.encrypt(text2))     
  print()
  text3=input('Enter string to be decrypted:')
  while tree.decrypt(text3)=='N':
      text3=input('Enter string to be decrypted:')
  print('Decrpted string: ',end='')     
  print(tree.decrypt(text3))     
main()

