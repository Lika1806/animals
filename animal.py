from abc import ABC, abstractmethod

class Animal(ABC):
    kind = 'kind'
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def eat(self):
        ...


class Fly(ABC):
    @abstractmethod
    def fly(self):
        ...

class Walk(ABC):
    @abstractmethod
    def walk(self):
        ...

class Swim(ABC):
    @abstractmethod
    def swim(self):
        ...

class Bird (Animal,Walk):
    wings = 'wings'

class Fish (Animal, Swim):
    fin = 'fin'
    def swim(self):
        print('swim')



