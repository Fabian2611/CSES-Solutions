s=input()
c=""
h=1
i=1
for v in s:
 if c==v:
  i+=1
 else:
    i=1
    c=v
 if i>h:h=i
print(h)