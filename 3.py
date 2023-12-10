class EvenNumbers:
    def __init__(self, n: int):
        self.n = n

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 2
        if self.i <= self.n:
            return self.i
        else:
            raise StopIteration


iterator = EvenNumbers(10)
for i in iterator:
    print(i)