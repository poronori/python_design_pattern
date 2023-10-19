# そのクラスのインスタンスが一つしか作成されない

def main():
    neko1 = Cat("ねこすけ")
    print("neko1={}".format(neko1.name))
    neko2 = Cat("ねこじろう")
    print("neko1={}, neko2={}".format(neko1.name, neko2.name))
    neko1.name = "ねこだったもの"
    print("neko1={}, neko2={}".format(neko1.name, neko2.name))

# singletonクラス
class Singleton(object):
    def __new__(cls, *args, **kargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# 実装クラス
class Cat(Singleton):
    def __init__(self, name):
        self.name = name

if __name__ == "__main__":
    main()