def test_generator01(end):
    yield list(range(end))


def test_generator02(end):
    yield from list(range(end))

    # yield from :


if __name__ == "__main__":
    test01 = test_generator01(10)

    for item in test01:
        print(item)

    test02 = test_generator02(10)

    for item in test02:
        print(item)
