print("Put the array of Directions speperated by spaces ")
txt = input()
list1=list(txt.split(" "))
x = True
#Removes unordered pair (NORTH,SOUTH) or (WEST, EAST) 
# after removing any pair it loop repeats from start to eliminate newly created pairs as well 
while x:
    try:
     for i in range(0,(len(list1)+1)):
      x=False   
      if (list1[i] == 'SOUTH' and list1[i-1] == 'NORTH') or (list1[i-1] == 'SOUTH' and list1[i] == 'NORTH'):
        list1.remove(list1[i])
        list1.remove(list1[i-1])
        x=True
        break
        
      if (list1[i] == 'EAST' and list1[i-1] == 'WEST') or (list1[i-1] == 'EAST' and list1[i] == 'WEST'):
        list1.remove(list1[i])
        list1.remove(list1[i-1])
        x=True
        break
    except:
     print()

print(list1)
