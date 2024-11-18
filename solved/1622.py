def f(t):
    if len(t)==1:
        return [t]
    r=[]
    for i,c in enumerate(t):
        for p in f(t[:i]+t[i+1:]):
            r.append(c+p)
    return r
t=list(set(f(input())))
t=[str(len(t))]+t
t.sort()
print("\n".join(t))