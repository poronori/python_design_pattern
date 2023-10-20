# クラスを拡張させる
# 既存クラスの機能を別枠で拡張することができる

def main():
    # 既存クラス
    cat = Animal(Cat())
    dog = Animal(Dog())
    cat.cry()
    dog.cry()
    
    # 機能追加クラス
    full_power_cat = FullPowerAnimal(Cat())
    full_power_dog = FullPowerAnimal(Dog())
    full_power_cat.full_power_cry()
    full_power_dog.full_power_cry()

# ======================================================
# 機能追加クラス
# ======================================================
# Bridge
class Animal():
    def __init__(self, animal_imple):
        self.animal = animal_imple
    
    def cry(self):
        self.animal.cry()

# 機能追加クラス
class FullPowerAnimal(Animal):
    def full_power_cry(self):
        print("全力で")
        self.animal.cry()

# ======================================================
# 既存クラス
# ======================================================
# 抽象クラス
class AnimalImple():
    def cry(self):
        pass

# 実装クラス
class Cat(AnimalImple):
    def cry(self):
        print("フヌン！")

class Dog(AnimalImple):
    def cry(self):
        print("わっふーん")

if __name__ == "__main__":
    main()