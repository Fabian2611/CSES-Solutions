inp = input()

substrs = set()

for i in range(len(inp)):
    for j in range(i + 1, len(inp) + 1):
        substrs.add(inp[i:j])

print(len(substrs))
