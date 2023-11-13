# インスタンスを共有することでリソースを無駄なく使う

def main():
    neko = Pet("ねこ")
    neko.call()
    neko2 = Pet("ねこ") # インスタンスは作成されない
    neko2.call()


# singletonクラス
class Singleton(object):
    def __new__(cls, *args, **kargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Factoryクラス
# インスタンスを返す
class PetFactory(Singleton):
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