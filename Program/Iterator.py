# Write a program to generate an iterator
class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current - 1
        else:
            raise StopIteration


# Create an instance of the iterator
my_iter = MyIterator(5)
for value in my_iter:
    print(value , end=' ')