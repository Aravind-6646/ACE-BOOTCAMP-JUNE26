from abc import ABC, abstractmethod
class AbstractClass(ABC):
    @abstractmethod
    def abcd(self):
        return "This is an abstract method"
class MainClass(AbstractClass):
    def abcd(self):
        return "This is the implementation of the abstract method"
m = MainClass()
print(m.abcd())    