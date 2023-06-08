class HelloStr:
    def __init__(self, name='홍길동', age=100):
        self.name = name
        self.age = age

    def __str__(self):
        return f'name : {self.name}\tage : {self.age}'

if __name__ == '__main__':
    class04 = HelloStr(name='이순신', age=10)
    print(class04)