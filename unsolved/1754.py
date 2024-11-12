input()
while True:
    try:
        i=input()
    except:
        break
    a,b=map(int,i.split())
    if a%2==0 ^ b%2==0 or a%3==0 and b%3==0:
        print("YES")
    else:
        print("NO")