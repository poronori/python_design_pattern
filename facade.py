# 複数クラス（処理）の窓口を作る

def main():
    # ペットの名前から最適なエサを取得する
    neko = PetFood("ねこまる")
    inu = PetFood("いぬじろう")
    sakana = PetFood("さかなくん")
    saru = PetFood("さるなーん")
    
    print(neko.getPetFood())
    print(inu.getPetFood())
    print(sakana.getPetFood())
    print(saru.getPetFood())

# ======================================================
# Facade
# ======================================================
# ペットの餌クラス
class PetFood():
    def __init__(self, name):
        self.name = name
    
    def getPetFood(self):
        kind = Pet(self.name).getKind()
        
        if kind == 1:
            return Cat().getFood()
        elif kind == 2:
            return Dog().getFood()
        elif kind == 3:
            return Fish().getFood()
        else:
            return "そんなペットは存在しない"

# ======================================================
# 複数クラス
# ======================================================
# ペットクラス
class Pet():
    def __init__(self, name):
        self.name = name
        
    def getKind(self):
        if self.name == "ねこまる":
            return 1
        elif self.name == "いぬじろう":
            return 2
        elif self.name == "さかなくん":
            return 3
        else:
            return 0

# 猫クラス
class Cat():
    def getFood(self):
        return "ねこ元気"
# 犬クラス
class Dog():
    def getFood(self):
        return "愛犬元気"
# 魚クラス
class Fish():
    def getFood(self):
        return "さかなのえさ"


if __name__ == "__main__":
    main()