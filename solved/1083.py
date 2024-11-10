input()
n=sorted(map(int,input().split()))
for i,l in enumerate(n,1):
 if i!=l:
  print(i)
  break
else:
 print(len(n)+1)