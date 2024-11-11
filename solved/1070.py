n=int(input())
if 1<n<4:
    print("NO SOLUTION")
elif n==1:
    print(1)
else:
    for i in range(2,n+1,2):
        print(i,end=" ")
    for i in range(1,n+1,2):
        print(i,end=" ")