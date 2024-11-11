input()
c=0
pi=-1
for i in map(int,input().split()):
    if i<pi:
        c+=pi-i
    else:
        pi=i
print(c)