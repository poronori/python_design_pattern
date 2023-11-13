# インスタンスを共有することでリソースを無駄なく使う

def main():
    pet = PetFactory()
    neko = pet.getPet("ねこ")
    neko.call()
    neko2 = pet.getPet("ねこ") # インスタンスは作成されない
    neko2.call()
    inu = pet.getPet("いぬ")
    inu.call()
    neko.call()

# singletonクラス
class Singleton(object):
    def __new__(cls, *args, **kargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Factoryクラス
# Petクラスを管理する
# 同じ引数であれば、新たにインスタンスを生成しない
class PetFactory(Singleton):
    petList = {}
    def getPet(self, name):
        self.pet = self.petList.get(name)
        if self.pet == None:
            self.pet = Pet(name)
            self.petList[name] = self.pet
        return self.pet

# ペットクラス
class Pet():
    def __init__(self, name):
        self.name = name
    
    def call(self):
        print(self.name)

if __name__ == "__main__":
    main()