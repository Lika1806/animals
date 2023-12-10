import animal

class Pinguin(animal.Bird, animal.Swim):
    kind = 'pinguin'
    def swim(self):
        print('swim for hunting')
    def walk(self):
        print('walk with shuffling')
    def eat(self):
        print('eat fish')

class Eagle(animal.Bird, animal.Fly):
    kind = 'eagle'
    def walk(self):
        print('walk with short steps')
    def eat(self):
        print('eat rabbit')
    def fly(self):
        print('fly')

class Tuna(animal.Fish):
    kind = 'tuna'
    def eat(self):
        print('hunt near surface')

class Flying_Fish(animal.Fish, animal.Fly):
    kind = 'flying_fish'
    def fly(self):
        print( 'flying beneath water')
    def eat(self):
        print( 'hunt in the water')

