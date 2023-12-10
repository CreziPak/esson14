def squares(n: int):
    for i in range(1, n + 1):
        yield i ** 2

print(type(squares))
generator = squares(10)
print(type(generator))
for i in generator:
    print(i)