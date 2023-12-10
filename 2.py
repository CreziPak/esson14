def squares(n: int):
    for i in range(1, (n // 2) + 1):
        yield i * 2

print(type(squares))
generator = squares(10000000)
print(type(generator))
for i in generator:
    print(i)