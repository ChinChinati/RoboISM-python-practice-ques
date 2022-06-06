x =[2]
n2 = int(input())

for i in range(2,n2+1):
    for j in x:
        if (i%j)==0:
            break
        if j == x[(len(x)-1)]:
            x.append(i)
print(x)

'''
for i in range(2,n2+1):
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
'''