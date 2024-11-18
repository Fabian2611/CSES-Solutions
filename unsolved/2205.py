s=list(map(bin,range(2**int(input()))))
for i in range(len(s)):
    print(s[i+1]) if i%2 else print(s[i])