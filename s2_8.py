a,b=map(int,input().split())
for i in range(a,b+1):
  temp=i
  sum=0
  while(temp>0):
    rem=temp%10
    sum+=rem**3
    temp=temp//10
    if sum==i:
      print(sum)
    
    
