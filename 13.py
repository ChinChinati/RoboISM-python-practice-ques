print("Put the array of intergers speperated by spaces ")
txt = input()

list1=list(txt.split(" "))
n=len(list1)
list2 = [0]*(n)


for i in range(0, n):
    list1[i] = int(list1[i])

'''list2 kepping count of each element
[1,1,1,1,1,...,2,1,..] only no. repeated will have value 2 in list2'''
for i in range(0,n):
    ele=(list1[i]-1)
    (list2[ele])=(list2[ele])+1

#print(list1)
#print(list2)
for i in range(0,n):
    if list2[i]== max(list2):
        print("Odd count no: "+str(i+1))
        break