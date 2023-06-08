class HelloFields:
    def __init__(self, name='홍길동', age=100):
        self.name = name
        self.age = age

    def member_info(self):
        return f'이름 : {self.name}\t나이 : {self.age}'

if __name__ == "__main__":
    class03 = HelloFields()
    print(class03.member_info())

    kim = HelloFields('김선달',50)
    print(kim.member_info())
