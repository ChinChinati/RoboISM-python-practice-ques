print("Put the array of intergers speperated by spaces ")
txt = input()
#making llist of all 100 numbers 
list1=list(txt.split(" "))
#empty list with 99 positions as main list has only 99 distinct numbers
# 1 of them is repeated
list2 = [0]*99

#converting all elements from string to interger
for i in range(0, 100):
    list1[i] = int(list1[i])

'''list2 kepping count of each element
[1,1,1,1,1,...,2,1,..] only no. repeated will have value 2 in list2
by finding position of 2 the duplicate no is found'''
for i in range(0,100):
    ele=(list1[i]-1)
    (list2[ele])=(list2[ele])+1

#print(list1)
#print(list2)
for i in range(0,100):
    if list2[i]==2:
        print("Repeated no. is: "+str(i+1))
        break