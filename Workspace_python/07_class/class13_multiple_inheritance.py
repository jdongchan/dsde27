class Lion:
    def bark(self):
        print('어흥')

class Eagle:
    def fly(self):
        print('파닥파닥')

class Griffin(Lion, Eagle):
    pass
# Griffin이 Lion과 Eagle을 상속받았음.
# 다중상속이라고 한다.
if __name__ == '__main__':
    griffin = Griffin()
    griffin.bark()
    griffin.fly()