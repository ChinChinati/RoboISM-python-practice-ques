print('Enter CC no.')
text = input()
while True:
 try:
  cc_number = int(text)
  if(len(str(cc_number))!=16 ):
    print('Enter a valid CC no.')
    cc_number = input()
  else: break

 except:
   print('Enter a valid CC no.') 
   text = input()

print('************'+str(cc_number)[12:17])
