class HelloFields:
    def __init__(self, name='홍길동', age=100): # class 호출 즉 인스턴스 생성시 인자를 받는 경우
        self.name = name
        self.age = age

    def member_info(self):
        return f'이름 : {self.name}\t나이 : {self.age}'

if __name__ == '__main__':
    class03 = HelloFields()
    print(class03.member_info())

    kim = HelloFields('김선달', 50)
    print(kim.member_info())

    class04 = HelloFields()
    print(class04.member_info())
    class05 = HelloFields(name='정동찬', age=29)
    print(class05.member_info())
    class05.name = '바보'  # 인스턴스 변수 수정
    print(class05.member_info())

