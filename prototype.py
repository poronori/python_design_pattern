# オブジェクトをコピーすることでオブジェクトを作る
# pythonの場合はcopy.deepcopy()を使うことで実現可能

def main():
    # たかしを生成
    original = Cat("たかし")
    
    # たかしのクローンを生成
    clones = []
    for num in range(10):
        clones.append(original.createClone())
    
    # 5番目だけ名前を変えてみる
    clones[4].name = "ミケランジェロ" 
    
    # 全員の名前を確認
    original.getName()
    for clone in clones:
        clone.getName()

# ======================================================
# インターフェース
# ======================================================
class Cloneable():
    def createClone(self):
        pass

# ======================================================
# 実装クラス
# ======================================================
# 猫クラス
class Cat(Cloneable):
    def __init__(self, name=None):
        self.name = name
    
    # コピーの作成
    def createClone(self):
        newCat = Cat()
        newCat.name = self.name
        return newCat
    
    def getName(self):
        print("私は" + self.name + "だ")

if __name__ == "__main__":
    main()