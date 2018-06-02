# File: ExpressionTree.py

#  Description: A program for ExpressionTree

#  Student's Name: Zongpeng Chen

#  Student's UT EID: zc3543
 
#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E 

#  Unique Number: 51335

#  Date Created:04/06/2018

#  Date Last Modified:04/11/2018

def is_operator(a):
    if a=='+' or a=='-' or a=='*' or a=='/':
      return True

def calculate(a,b,item):
    if item=='+':
      return float(a)+float(b)
    if item=='-':
      return float(a)-float(b)
    if item=='*':
      return float(a)*float(b)
    if item=='/':
      return float(a)/float(b)

def is_num(item):
    Flag=False
    if item.count('.')==1:
        tes=item.replace('.','')
        if tes.isdigit():
            Flag=True
    if item.isdigit():
        Flag=True
    return Flag

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append (item)

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check the item on the top of the stack
  def peek (self):
    return self.stack[-1]

  # check if the stack is empty
  def is_empty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))

  def remove(self,a):
    self.stack.remove(a)
    
  def count(self,a):
    return self.stack.count(a)

class Node (object):
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None
        self.parent=None

class Tree (object):
  def __init__ (self):
    self.root=None
    self.stack=Stack()
    
  def createTree (self, expr):
   self.origin=expr
   current=self.root
   for i in range(len(expr)):
      Flag=False
      if expr[i].count('.')==1:
          tes=expr[i].replace('.','')
          if tes.isdigit():
              Flag=True 
      if current!=None:
          parent=current.parent
      new_node=Node(expr[i])
      if expr[i]=='(':
          if self.root==None:
              self.root=new_node
              new_node.lchild=Node('(')
              parent=new_node
              new_node.parent=None
              current=new_node.lchild
              current.parent=parent
          else:
              if parent.data=='(':
                  current.lchild=new_node
                  new_node.parent=current
                  parent=current
                  current=current.lchild
                  current.parent=parent
              elif is_operator(parent.data):
                  parent.rchild=new_node
                  new_node.parent=parent
                  current=new_node
                  parent=current
                  current.lchild=Node('(')
                  current.lchild.parent=current
                  current=current.lchild 
      if expr[i].isdigit() or Flag==True:
        if parent.data=='(':
            parent.lchild=Node(expr[i])
            parent.lchild.parent=parent
            current=parent
        else:
            parent.rchild=Node(expr[i])
            parent.rchild.parent=parent
            current=parent
      if expr[i]=='+' or expr[i]=='-' or expr[i]=='*' or expr[i]=='/':
          if current.parent==None:
              previous=current
              self.root=new_node
              current=new_node
              current.lchild=previous.lchild
              previous.lchild.parent=current
              current.rchild=Node('(')
              current.rchild.parent=current
              current.parent=parent
              parent=current
              current=current.rchild
          else:
              if not is_operator(current.data):
                  if current.parent.lchild.data=='(':
                    current.parent.lchild=new_node
                    new_node.lchild=current.lchild
                    current.lchild.parent=new_node
                    new_node.parent=current.parent
                    current=new_node
                    current.rchild=Node('(')
                    parent=current
                    current=current.rchild
                    current.parent=parent
                  else:
                    current.parent.rchild=new_node
                    new_node.lchild=current.lchild
                    current.lchild.parent=new_node
                    new_node.parent=current.parent
                    current=new_node
                    current.rchild=Node('(')
                    parent=current
                    current=current.rchild
                    current.parent=parent
                  
              else:
                  current.parent.rchild=new_node
                  new_node.parent=current.parent
                  current=new_node
                  current.rchild=Node('(')
                  parent=current
                  current=current.rchild
                  current.parent=parent
      if expr[i]==')':
            current=parent
            
  def evaluate (self, aNode):
      operators=['+','-','*','/']
      expr=[]
      if aNode==self.root:
          expr=self.origin
      for item in expr:
          if item=='(':
              self.stack.push('(')
          if is_num(item):
              self.stack.push(item)
          if item in operators:
              self.stack.push(item)
          if item==')':
              oper2=self.stack.pop()
              while not is_num(oper2):
                  oper2=self.stack.pop()
              token=self.stack.pop()
              while not is_operator(token):
                 token=self.stack.pop() 
              oper1=self.stack.pop()
              while not is_num(oper1):
                  oper1=self.stack.pop()
              self.stack.push(str(calculate(oper1,oper2,token)))
      num1=self.stack.count('(')
      for i in range(num1):
          self.stack.remove('(')
      len1=0
      for item in expr:
        if item.count('.')==1:
            inde=item.index('.')
            str1=''
            for i in range(inde+1,len(item)):
                str1+=item[i]
            len2=len(str1)
            if len2>len1:
                len1=len2
      valueo=self.stack.pop()
      valueof=float(valueo)
      if int(valueof)==valueof:
        valueo=str(int(valueof))
      else:
        valueo=round(valueof,len1)
        valueo=str(valueo)
      return valueo
    
  def preOrder (self, aNode):
    if (aNode != None):
      print (aNode.data,end=' ')
      self.preOrder (aNode.lchild)
      self.preOrder (aNode.rchild)
      
  def postOrder (self, aNode):
      if aNode!=None:
        self.postOrder(aNode.lchild)
        self.postOrder(aNode.rchild)
        print(aNode.data,end=' ')
 
def main():
    print()
    filevar=open('expression.txt','r')
    a=filevar.readline()
    a=a.strip()
    a=a.split(' ')
    exp=[]
    for item in a:
      exp.append(item)
    tree=Tree()
    tree.createTree(exp)
    str1=''
    for item in exp:
        str1+=item
        str1+=' '
    valueo=tree.evaluate(tree.root)
    print(str1+'= '+valueo)
    print()
    print('Prefix Expression: ',end='')
    tree.preOrder(tree.root)
    print()
    print()
    print('Postfix Expression: ',end='')
    tree.postOrder(tree.root)
main()
