_,x=input().split()
p=input().split()
p.sort()
c=1
i=0
while i<len(p):
    if i<len(p)-1 and p[i]+p[i+1]:
        c+=1
        i+=2
    else:
        c+=len(p)-i
        break
print(c)