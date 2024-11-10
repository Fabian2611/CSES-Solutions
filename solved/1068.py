n: int = int(input())
values: list[str] = [str(n)]

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    values.append(str(n))

print(" ".join(values))
