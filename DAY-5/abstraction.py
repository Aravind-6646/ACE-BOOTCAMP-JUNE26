from abc import ABC
class Animal(ABC):
    def eat(self):
        pass
    #@staticmethod
    def sleep(self):
        return "I am sleeping..."
class Dog:
    a=Animal()    