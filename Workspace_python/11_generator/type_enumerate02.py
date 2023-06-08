class MyEnumerate:
    def my_enumerate(iterable):
        i = 0
        for item in iterable:
            yield i, item
            i += 1


if __name__ == "__main__":
    subjects = MyEnumerate.my_enumerate(["python", "ds", "de"])
    print(subjects)

    for i, item in subjects:
        print(f"{i} 번지 : {item}")
