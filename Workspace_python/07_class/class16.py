from abc import ABCMeta, abstractmethod

# metaclass : class를 만들어주는 class
class AbstractParent(metaclass=ABCMeta):
    def prn(self):
        print('abstract class')

    def abstract_method(self):
        pass

class child(AbstractParent):
    def abstract_method(self):
        print('abstract method override')

if __name__ == '__main__':
    child = Child()
    child.prn()
    child.abstract_method()