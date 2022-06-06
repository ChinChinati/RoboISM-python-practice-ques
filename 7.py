print("Put the array of elements speperated by spaces ")
txt = input()
list1=list(txt)

n = 0
element = list1[0]
for i in list1:
    frequency = list1.count(i)
    if frequency > n:
        n = frequency
        element = i
      
# printing result
print ("Most frequent number is : " + str(element))
