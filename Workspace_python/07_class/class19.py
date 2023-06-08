from abc import *

class Character(metaclass = ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def attack(self):
        pass

class Knight(Character):
    def attack(self):
        print(f'{self.name} : 칼로 공격!')

class Archer(Character):
    def attack(self):
        print(f'{self.name} : 활로 공격!')

if __name__ == '__main__':
    character = None

    # 동적 바인딩 : 필요한 순간에 객체 만들어 사용할거야.
    select = int(input('1:기사\n2:궁수\n직업을 선택해 주세요 : '))

    match select:
        case 1:
            character = Knight('척준경')
        case 2:
            character = Archer('주몽')
    # polymorphism - 다형성
    character.attack()

