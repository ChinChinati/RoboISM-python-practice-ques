p =int(input()) 
q =int(input()) 
n2=max(p,q)
n1=min(p,q)
def do(x,y):   
     r =x%y
     if r==0: 
         print('GDC'+str(y)) 
         exit()
     x =int(x/y)
     do(y,r)
do(n2,n1)

