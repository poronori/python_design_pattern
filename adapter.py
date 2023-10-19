# インターフェースの互換性のないものどうしを組み合わせる
# 別のクラスを同じインターフェースに落とし込むことができる

def main():
    
    cat = Cat() # インターフェース実装済みクラス
    dog = DogAdapter() # Adapter
    
    print("ねこのターン")
    cat.Action()
    cat.Looks()
    cat.Rest()
    
    print("いぬのターン")
    dog.Action()
    dog.Looks()
    dog.Rest()

# Adaptee　既存クラス
class Dog():
    def Cry(self):
        print("わんわん！")
    
    def Walk(self):
        print("散歩中")
    
    def Sit(self):
        print("おすわり")
    
    def Size(self):
        print("でかい")
    
    def Sleep(self):
        print("おやすみなさい")
    
    def Wait(self):
        print("待て")

# Target インターフェース
class Animal():
    def Action(self):
        pass
    
    def Looks(self):
        pass
    
    def Rest(self):
        pass

# Targetを実装している既存クラス
class Cat(Animal):
    def Action(self):
        print("ニャー")
    
    def Looks(self):
        print("小さめ")
    
    def Rest(self):
        print("おやすみにゃさい")


# Adapter 既存クラスとTargetをつなげる
class DogAdapter(Animal):
    def __init__(self):
        self.dog = Dog()
    
    def Action(self):
        self.dog.Cry()
        self.dog.Walk()
        self.dog.Wait()
    
    def Looks(self):
        self.dog.Size()
    
    def Rest(self):
        self.dog.Sit()
        self.dog.Sleep()


if __name__ == "__main__":
    main()