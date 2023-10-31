# 機能をかぶせる

def main():
    bigCat = BigAnimal(Cat())
    bigDog = BigAnimal(Dog())
    smallCat = SmallAnimal(Cat())
    smallDog = SmallAnimal(Dog())
    
    print(bigCat.getKind())
    print(bigDog.getKind())
    print(smallCat.getKind())
    print(smallDog.getKind())

# ======================================================
# Component（インターフェース）
# ======================================================
# 動物クラス
class Animal():
    def getKind(self):
        pass

# ======================================================
# 実装クラス
# ======================================================
# 猫クラス
class Cat(Animal):
    def getKind(self):
        return "猫"

# 犬クラス
class Dog(Animal):
    def getKind(self):
        return "犬"

# ======================================================
# Decorator
# ======================================================
# 大きい動物クラス
class BigAnimal(Animal):
    def __init__(self, animal:Animal):
        self.animal = animal
    
    def getKind(self):
        name = "大きな"
        name += self.animal.getKind()
        return name

# 小さい動物クラス
class SmallAnimal(Animal):
    def __init__(self, animal:Animal):
        self.animal = animal
    
    def getKind(self):
        name = "小さな"
        name += self.animal.getKind()
        return name

if __name__ == "__main__":
    main()