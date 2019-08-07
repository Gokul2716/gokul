n=int(input())
facto=1
if n>0:
  for i in range(1,n+1):
    facto=facto*i
elif n==0:
  facto=1
print(facto)
