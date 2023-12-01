# 各要素に順番にアクセスする
# pythonは__iter__と__next__を使えば実現できるが、今回はあえて使わない

def main():
    animals = AnimalHouse()
    animals.appendAnimal("ねこちゃん")
    animals.appendAnimal("こいぬくん")
    animals.appendAnimal("さかなさん")
    animals.appendAnimal("ちんちらさま")
    
    iterator = animals.iterator()
    while(iterator.hasNext()):
        animal = iterator.next()
        print(animal)

# ======================================================
# 抽象クラス
# ======================================================
class Aggregate():
    def iterator(self):
        pass
class Iterator():
    def hasNext():
        pass
    
    def next():
        pass

# ======================================================
# 実装クラス
# ======================================================
class AnimalHouse(Aggregate):
    
    def __init__(self):
        self.animals = []
        self.last = 0
    
    def getAnimal(self, index):
        return self.animals[index]
    
    def appendAnimal(self, name):
        self.animals.append(name)
        self.last += 1
    
    def getLength(self):
        return self.last
    
    def iterator(self):
        return AnimalIterator(self)

class AnimalIterator(Iterator):
    def __init__(self, animalHouse):
        self.animal = animalHouse
        self.index = 0
    
    def hasNext(self):
        if self.index < self.animal.getLength():
            return True
        else:
            return False
    
    def next(self):
        animal = self.animal.getAnimal(self.index)
        self.index += 1
        return animal

if __name__ == "__main__":
    main()