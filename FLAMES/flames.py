hell=['Friends','Lovers','Affection','Marriage','Enemy','Sister']
def commonchar(name1,name2):
   x=len(set(name1) & set(name2))
   y=((len(name1))+(len(name2)))-(2*x)
   return y
def Flames(hell,r):
    z =(r%7)-1
    if len(hell)==1:
       return hell[0]
    else :
       a=hell.pop(z)
       b=hell[-z:]+hell[:-z]
       return Flames(b,r)
name1=input("Enter the first name:")
name2=input("Enter the second name:")
d=commonchar(name1,name2)
m=Flames(hell,d)
print("The relationship between",name1,"and",name2,"is",m)
