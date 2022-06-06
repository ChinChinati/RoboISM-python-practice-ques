print("Enter x:")
x = int(input())
print("Enter of y:")
y = int(input())

x = x ^ y
y = x ^ y
x = x ^ y
print("Value of x:", x)
print("Value of y:", y)