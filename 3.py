print("Enter first no.")
a=int(input())
print("Enter operator")
op=input()
print("Enter second no.")
b=int(input())

if op=='+':
    c=a+b
if op=='-':
    c=a-b
if op=='.':
    c=a*b
if op=='/':
    c=a/b 

print("a"+str(op)+"b="+str(c))