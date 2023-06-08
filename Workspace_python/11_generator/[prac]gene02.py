def subject_generator():
    yield "python"
    yield "machine learning"
    yield "big data"


if __name__ == "__main__":
    subjects = subject_generator()
    print(type(subjects))
    print(subjects.__next__()) # 첫번째값
    print(next(subjects)) # 두번째값
    print(next(subjects)) # 세번째값

    li = []
    for i in subjects: # 3개 다 뽑아서 남은 값이 없음.
        li.append(i)
    print(li) # 리스트에도 아무것도 없겠지.

