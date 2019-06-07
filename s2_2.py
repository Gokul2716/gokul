n=int(input())
a=n
res=0
while(n!=0):
  rev=n%10
  res=res*10+res
  n=n//10
  
if(a==res):
  print("yes")
else:
  print("no")
