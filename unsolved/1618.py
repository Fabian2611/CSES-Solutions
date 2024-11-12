def fac(n):
    if n==1:return 1
    return n*fac(n-1)
a=str(fac(int(input())))
print(len(a)-len(a.rstrip("0")))