class MyIter:

    def __init__(self, end):
        self.start = 0
        self.end = end
        self.val = 1

    def __iter__(self):
        return self

    # This method is called when an iterator is required for a container.
    # This method should return a new iterator object that can iterate over all the objects in the container.
    # For mappings, it should iterate over the keys of the container.

    def __next__(self):
        self.start += 1
        if self.start <= self.end:
            self.val = self.start ** 2
            return self.val
        else:
            raise StopIteration

    # Return the next item from the iterator.
    # If there are no further items, raise the StopIteration exception.
    # This method corresponds to the tp_iternext slot of the type structure for Python objects in the Python/C API.

    def __getitem__(self, item):
        if item < self.end:
            return list(self)[item]
        else:
            raise IndexError
    # Return an object representing the specialization of a generic class by type arguments found in key.
    # When defined on a class, __class_getitem__() is automatically a class method.
    # As such, there is no need for it to be decorated with @classmethod when it is defined.

if __name__ == '__main__':
    for i in MyIter(10):
        print(i)

    print(list(MyIter(15)))
    print(MyIter(15[15]))

