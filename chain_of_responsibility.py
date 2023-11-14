# たらい回し、役割分担
# 処理を要求する側と処理を行う側の結びつきを弱めることができる

def main():
    # 飼いたいペット候補
    mouse = Pet("ねずこ", 1)
    cat = Pet("ねここ", 3)
    dog = Pet("いぬお", 8)
    lion = Pet("らいお", 15)
    
    # 部屋探し
    room = SmallRoom(MiddleRoom(BigRoom())) # 小さい部屋から順番にチェック
    room.searchRoom(mouse)
    room.searchRoom(cat)
    room.searchRoom(dog)
    room.searchRoom(lion)

# ======================================================
# Handler 抽象クラス
# ======================================================
# 部屋クラス
class Room():
        
    def __init__(self, room = None):
        self.room = room
    
    def searchRoom(self, pet):
        if self.room is not None:
            self.room.searchRoom(pet)
        else:
            print("そんな大きなペットは飼えません。")

# ======================================================
# ConcreteHandler 実装クラス
# ======================================================
class SmallRoom(Room):
    capacity = 1
    def searchRoom(self, pet):
        if pet.size <= self.capacity:
            print("{}を小さい部屋に飼う".format(pet.name))
        else:
            super().searchRoom(pet)
class MiddleRoom(Room):
    capacity = 5
    def searchRoom(self, pet):
        if pet.size <= self.capacity:
            print("{}を中くらいの部屋に飼う".format(pet.name))
        else:
            super().searchRoom(pet)
            
class BigRoom(Room):
    capacity = 10
    def searchRoom(self, pet):
        if pet.size <= self.capacity:
            print("{}を大きい部屋に飼う".format(pet.name))
        else:
            super().searchRoom(pet)

# ペットクラス
class Pet():
    def __init__(self, name, size):
        self.name = name # 名前
        self.size = size # 大きさ

if __name__ == "__main__":
    main()