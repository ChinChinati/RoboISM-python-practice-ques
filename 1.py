
list1=input("Enter list: ")
list1=list(list1.split(" "))
print(list1)
for i in range(0, len(list1)):
    list1[i] = int(list1[i])
s=input("String: ")

if s=="asc" or s=="desc":
    list1.sort()
    if s=="desc":
        list1.reverse()
    print(list1)

if s=="none":
    print(list1)