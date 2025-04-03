#single level inheritance

class Animal:
    def __init__(self,name, speci):
        self.name=name
        self.speci=speci

    def makesound(self):
        print(f"sound made by the animal!")


class Cat(Animal):
    def __init__(self,name, breed):
        super().__init__(name,speci="Cat")
        self.breed=breed

    def makesound(self):
        print("MEOW MEOW..")


ani=Animal("harry","dog")
ani.makesound()
cat1=Cat("jack","cat food")
cat1.makesound()

