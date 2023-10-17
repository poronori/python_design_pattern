# オブジェクト作成時に、作成するオブジェクトのクラスをサブクラスに選ばせる

def main():
    cat = CatFactory()
    dog = DogFactory()
    
    cat.create_animal()
    dog.create_animal()

# ======================================================
# 抽象基底クラス Creator
# ======================================================
class Factory():
    def __init__(self):
        self.animal = self.factory_method()
    
    def create_animal(self):
        self.animal.looks()
        self.animal.cry()
        self.animal.size()
    
    def factory_method(self):
        pass

# 動物クラス　Product
class Animal():
    def looks(self):
        pass
    
    def cry(self):
        pass
    
    def size(self):
        pass

# ======================================================
# 生成クラス ConcreteCreator
# ======================================================
# 猫生成クラス
class CatFactory(Factory):
    def factory_method(self):
        return Cat()
# 犬生成クラス
class DogFactory(Factory):
    def factory_method(self):
        return Dog()

# ======================================================
# 実装クラス ConcreteProduct
# ======================================================
# 猫クラス
class Cat(Animal):
    def looks(self):
        print("かわいい")
    
    def cry(self):
        print("ニャオニャオ！！！")
    
    def size(self):
        print("ちょっと大きい")

# 犬クラス
class Dog(Animal):
    def looks(self):
        print("かっこいい")
    
    def cry(self):
        print("バウワウ")
    
    def size(self):
        print("でかすぎんだろ")

if __name__ == "__main__":
    main()