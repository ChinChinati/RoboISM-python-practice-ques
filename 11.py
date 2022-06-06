print("Enter a string:")
string = input()
n = len(string)

if n%2 == 0:
    s1 = string[:int((n/2))]
    s2 = string[int((n/2)):][::-1]
else:
    s1 = string[:int((n-1)/2)]
    s2 = string[int((n+1)/2):][::-1]

if s1.lower() == s2.lower():
    print("The strings is a Palindrome")
else:
    print("The strings isn't a Palindrome")
