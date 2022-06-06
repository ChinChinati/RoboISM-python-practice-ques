import random 
x= random.randint(1000,9999)
x= str(x)
print(x)
for n in range(0,10):

 result = ['B' ,'B', 'B', 'B']
 inp=str(input())
 for i in range(0,4):
   for j in range(0,4):
    if inp[i] == x[i]:
     result[i] = 'R'
    elif inp[i] == x[j]:
     result[i] = 'Y'
    
 if result== ['R', 'R', 'R', 'R']:
   print('WON')
   exit()
 print(result)