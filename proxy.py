# 代理人を扱う
# オブジェクトのアクセス制限、生成の遅延などを行える

def main():
    childOwner = Child()
    childOwner.feeding()  # => 適当に餌を与える
    childOwner.cleaning() # => 隅々まで掃除する
    childOwner.love()     # => かわいがる
    
    parentsOwner = Parents()
    parentsOwner.feeding()  # => 最高級の餌を与える
    parentsOwner.cleaning() # => 隅々まで掃除する
    parentsOwner.love()     # => 愛情を与える
    
# ======================================================
# Subject 抽象クラス
# ======================================================
# 飼い主クラス
class Owner():
    # 餌やり
    def feeding(self):
        pass
    # 掃除
    def cleaning(self):
        pass
    # かわいがる
    def love(self):
        pass

# ======================================================
# RealSubject 実装クラス
# ======================================================
# 親クラス
class Parents(Owner):
    def feeding(self):
        print("最高級の餌を与える")
    def cleaning(self):
        print("隅々まで掃除する")
    def love(self):
        print("愛情を与える")

# ======================================================
# Proxy
# ======================================================
# 子どもクラス
class Child(Owner):
    def feeding(self):
        print("適当に餌を与える")
    def cleaning(self):
        # 子どもは掃除が苦手なので親にやってもらう
        Parents().cleaning()
    def love(self):
        print("かわいがる")

if __name__ == "__main__":
    main()