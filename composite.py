# 容器と中身を同一視する
# ファイルシステムの場合、フォルダを消すときにファイルなのかフォルダなのか意識せずに消すことができる

def main():
    myHouse = House("我が家")
    neko = Pet("猫")
    inu = Pet("犬")
    tokage = Pet("コモドオオトカゲ")
    hanare = House("離れ")
    zou = Pet("象")
    kirin = Pet("キリン")
    
    myHouse.add(neko)
    myHouse.add(inu)
    myHouse.add(tokage)
    hanare.add(zou)
    hanare.add(kirin)
    myHouse.add(hanare)
    
    myHouse.remove()

# Component（抽象クラス）
class AbstractHouse():
    def __init__(self, name):
        self.name = name
    
    def remove():
        pass

# Composite（容器）
# 家クラス
class House(AbstractHouse):
    def __init__(self, name):
        self.name = name
        self.list = []
    
    def add(self, item:AbstractHouse):
        self.list.append(item)
        print("{}を購入しました".format(item.name))
        
    def remove(self):
        itr = iter(self.list)
        for item in itr:
            item.remove()
        print("{}を処分しました".format(self.name))

# Leaf（中身）
# ペットクラス
class Pet(AbstractHouse):
    def __init__(self, name):
        self.name = name
    
    def remove(self):
        print("{}を処分しました".format(self.name))

if __name__ == "__main__":
    main()