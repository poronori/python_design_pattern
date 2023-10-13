# インスタンスの生成を専門に行うクラスを用意することで、間違いないように（複雑な）オブジェクトをつくる

def main():
    dogFactory = AbstractFactory().createFactory(DogFactory.id, "イヌコ")
    catFactory = AbstractFactory().createFactory(CatFactory.id, "ネコオ")
    
    dogFactory.getCry().cry()
    dogFactory.getColor().color()
    dogFactory.getSize().size()
    
    catFactory.getCry().cry()
    catFactory.getColor().color()
    catFactory.getSize().size()

# ======================================================
# 抽象基底クラス
# ======================================================
class AbstractFactory:
    def createFactory(self, id, name):
        if id == 1:
            return DogFactory(name)
        elif id == 2:
            return CatFactory(name)
        else:
            return
    
    def getCry():
        pass
    
    def getColor():
        pass
    
    def getSize():
        pass

# 抽象クラス１（鳴き声）
class AbstractCry:
    def __init__(self, name):
        self.name = name
    
    def cry():
        pass

# 抽象クラス２（色）
class AbstractColor:
    def __init__(self, name):
        self.name = name
    
    def color():
        pass

# 抽象クラス３（大きさ）
class AbstractSize:
    def __init__(self, name):
        self.name = name
    
    def size():
        pass

# ======================================================
# 犬クラス
# ======================================================
class DogFactory(AbstractFactory):
    id = 1
    
    def __init__(self, name):
        self.name = name
    
    def getCry(self):
        return DogCry(self.name)
    
    def getColor(self):
        return DogColor(self.name)
    
    def getSize(self):
        return DogSize(self.name)

# 犬の鳴き声クラス
class DogCry(AbstractCry):
    def cry(self):
        print(self.name + "：ワン！")
# 犬の色クラス
class DogColor(AbstractColor):
    def color(self):
        print(self.name + "：黒色")
# 犬の大きさクラス
class DogSize(AbstractSize):
    def size(self):
        print(self.name + "：身長100cm")

# ======================================================
# 猫クラス
# ======================================================
class CatFactory(AbstractFactory):
    id = 2
    
    def __init__(self, name):
        self.name = name
    
    def getCry(self):
        return CatCry(self.name)
    
    def getColor(self):
        return CatColor(self.name)
    
    def getSize(self):
        return CatSize(self.name)

# 猫の鳴き声クラス
class CatCry(AbstractCry):
    def cry(self):
        print(self.name + "：ミャオ！")
# 猫の色クラス
class CatColor(AbstractColor):
    def color(self):
        print(self.name + "：茶色")
# 猫の大きさクラス
class CatSize(AbstractSize):
    def size(self):
        print(self.name + "：身長150cm")


if __name__ == "__main__":
    main()