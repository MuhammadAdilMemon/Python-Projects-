#here child is gonna have multiple parents

class Animal:
    def __init__(self,name, speci):
        self.name=name
        self.speci=speci

    def makesound(self):
        print("whatever sound animal makes")



class Mammal:
    def __init__(self,name,fur_colour):
        self.name=name
        self.fur_colour=fur_colour


class Dog(Animal,Mammal):
    def __init__(self,name,breed,fur_colour):
        Animal.__init__(self,name,speci="Dog")
        Mammal.__init__(self,name,fur_colour)
        self.breed=breed

    def makesound(self):
        print("bhow bhow..")


dg=Dog("husky","bones","grey")
dg.makesound()