a,b=map(int,input().split())
for i in range(a+1,b):
  if(i>0):
      for j in range(2,i):
          if(i%j==0):
              break
      else:
          print(i,end=" ")
              
