y = []#all numbers
x =[] #non prime no.
#prime no. = y -x
n1 = int(input())
n2 = int(input())
  
for i in range(n1,n2+1):
    y.append(i)
    for j in range(2,i): 
       r = i%j
       if r == 0:
           x.append(i)
           break
for i in x:
  if i in y:
    y.remove(i)
print(y)
