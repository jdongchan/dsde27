from abc import ABC, abstractmethod

# ABC : Abstract Base Class

class AbstractClass(ABC): # 추상 메서드를 가진 클래스를 추상클래스라고 한다.
    def prn(self):
        print('abstract class : abstract method를 하나 이상 가질 수 있는 클래스')

    @abstractmethod # 함수의 껍데기만 있고 실제 내용이 없다. -> abs method라고 한다.
    # 아직 무슨 내용을 추가할지 모를 때, 세부적인 내용이 필요없을 때
    def abstract_method(self):
        pass

class Child(AbstractClass):
    def abstract_method(self):
        print('abstract method : 상속받는 자식 클래스가 반드시 구현!')

if __name__ == '__main__':
    # 추상 클래스는 객체화 불가!
    # abstract_parent = AbstractClass()
    # abstract_parent.abstract_method()

    child = Child()
    child.prn()
    child.abstract_method()