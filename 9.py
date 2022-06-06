asci=[]
x = []
txt=input()
list1 = (list(txt))
for i in range(0, len(list1)):
    asci.append(ord(list1[i]))
#asci list contains list of ascii values of string characters
    
asci.sort()
for i in range(0, len(asci)):
   x.append(chr(asci[i]))
x= ''.join(x)
print(x)