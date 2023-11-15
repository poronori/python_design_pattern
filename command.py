# 個々の処理を一つのコマンドとしてまとめる
# オブジェクトを引数に渡すことで、要求に応じて複数組み合わせで使うことができる

def main():
    # コマンドをセット
    cat = CompositeCommand()
    cat.appendCommand(EatCommand("ねこ元気"))
    cat.appendCommand(CryCommand("にゃおにゃお"))
    cat.appendCommand(ActionCommand("尻尾を振る"))
    # コマンドを起動
    cat.execute()
    
    # コマンド単体でも動かせる
    dog = EatCommand("愛犬元気")
    dog.execute()

# ======================================================
# Command 抽象クラス
# ======================================================
class Command():
    def execute(self):
        pass

# ======================================================
# ConcreteCommand 実装クラス
# ======================================================
class EatCommand(Command):
    def __init__(self, food):
        self.food = food
    
    def execute(self):
        print("{}を食べる".format(self.food))
class CryCommand(Command):
    def __init__(self, cry):
        self.cry = cry
        
    def execute(self):
        print(self.cry)
class ActionCommand(Command):
    def __init__(self, action):
        self.action = action
    
    def execute(self):
        print(self.action)

# ======================================================
# Invoker 起動者
# ======================================================
class CompositeCommand(Command):
    def __init__(self):
        self.command = []
    
    def appendCommand(self, command):
        self.command.append(command)
    
    def execute(self):
        for cmd in self.command:
            cmd.execute()

if __name__ == "__main__":
    main()