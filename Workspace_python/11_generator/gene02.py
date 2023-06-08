def subject_generator():
    yield "python"
    yield "machine learning"
    yield "big data"


if __name__ == "__main__":
    subjects = subject_generator()
    print(type(subjects))

    for item in subjects:
        print(item)

    print(list(subject_generator()))
