from Pifentry import pifentry
from BST import BST

ST=BST()
file1 = open('pb1.txt', 'r')
Lines = file1.readlines()
ST_POS=0
PIF=[]
reserved=["Var","int","bool",":",";","input","(",")","if","print","else","<",">","=","+","-","*","/","and","{","}","for","true","false","%"]
def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

for line in Lines:
   deliminators=[";"," ",":",",","(",")","<",">","=","+","-","*","/","{","}","%"]
   tokens = []
   token=""
   for char in line:
       token=token+char
       if char in deliminators:
           tokens.append(token[:-1])
           token=""
           if(token!=" "):
            tokens.append(char)
   tokens=remove_values_from_list((remove_values_from_list(tokens," ")),"")



   for i in tokens:
       if i in reserved:
           PIF.append(pifentry(i,-1))
       else:
           if(ST.search(i))==-1:
               if(i.isnumeric()):
                   PIF.append(pifentry("Const", ST.counter))
               else:
                   PIF.append(pifentry("Id",ST.counter))
               print(i)
               ST.insert(i)
           else:
               PIF.append(pifentry("ID",ST.search(i)))

file1 = open('pb1PIF.txt', 'w')
file2 = open('pb1ST.txt', 'w')
for i in PIF:
    file1.write(str(i.token)+" "+str(i.st_pos)+"\n")
file1.close()
ST.print_tree(file2)
