def my_generator(end):
    i = 0
    while i < end:
        i += 1

        yield i ** 2


if __name__ == "__main__":
    nums = my_generator(10)
    print(nums)

    print(nums.__next__())
    print(nums.__next__())
    print(nums.__next__())
    print(next(nums))

    for item in nums:
        print(item)
