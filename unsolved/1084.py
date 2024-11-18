# SOLVED but timeout
x=lambda _:list(map(int,input().split()))
*q,k=x(0)
s=x(0)
m=x(0)
c=0
for i in m:
    for j in range(len(s)):
        if i-k<=s[j]<=i+k:
            c+=1
            s.pop(j)
            break
print(c)