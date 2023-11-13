# インスタンスを共有することでリソースを無駄なく使う

def main():
    neko = PetFactory("ねこ")
    neko.getPet().call()
    neko2 = PetFactory("ねこ") # インスタンスは作成されない
    neko2.getPet().call()
    inu = PetFactory("いぬ")
    inu.getPet().call()

# singletonクラス
class Singleton(object):
    def __new__(cls, *args, **kargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Factoryクラス
# Petクラスを管理する
# 同じ引数であれば新たにインスタンスを生成しない
class PetFactory(Singleton):
    petList = {}
    def __init__(self, name):
        self.pet = self.petList.get(name)
        if self.pet == None:
            self.pet = Pet(name)
            self.petList[name] = self.pet
    
    def getPet(self):
        return self.pet

# ペットクラス
class Pet():
    def __init__(self, name):
        self.name = name
    
    def call(self):
        print(self.name)

if __name__ == "__main__":
    main()