def my_range(start=0, stop=0, step=1):
    while start < stop:
        yield start
        start += step


if __name__ == "__main__":
    print(list(my_range(stop=10)))
    print(list(my_range(start=5, stop=100, step=5)))
