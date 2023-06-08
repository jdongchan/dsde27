class Person:
    def prn(self):
        print('person')

class Father(Person):
    def prn(self):
        print('father')

class Mother(Person):
    def prn(self):
        print('mother')

class Child(Father, Mother):
    # father가 먼저 써져있음.
    pass
# 다이아몬드 상속
# Child가 부모의 prn을 호출했을 때 F와 M 중 어디 것을 상속받을 것 인가?
# 먼저 입력해놓은 부모를 상속받는다. 그리고 더 가까운 것을 찾는다.

if __name__ == '__main__':
    child = Child()
    child.prn()
    # Method Resolution Order (MRO) : 메서드 탐색 순서
    print(Child.mro())


'''
오늘의 복습
class
-> 속성
    -class variable
    -instance variable
-> 기능
    -@classmethod : (cls) 
    -@staticmethod : !
    -instance method : self
    
inheritance
-> override (재정의)

python에서의 최상위 객체 : object

mro : 다중 상속일 때, 메서드 탐색 순서
'''