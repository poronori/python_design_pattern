# 特定の言語やルールで書かれた文字を解析し、適した処理を行う

def main():
    text = "えさ,えさ,待て,えさ,aaaa"
    context = Context(text)
    context.BuildExpression()

# 処理対象
class Context():
    def __init__(self, context):
        self.text = context.split(',')
    
    def BuildExpression(self):
        for text in self.text:
            expression = IExpression().GetExpression(text)
            expression.Operate()

# 処理
class IExpression():
    
    def GetExpression(self, text):
        if text == "えさ":
            return Feed()
        elif text == "待て":
            return Wait()
        else:
            return Else()
    
    def Operate(self):
        pass

class Feed(IExpression):
    def Operate(self):
        print("えさをやる")

class Wait(IExpression):
    def Operate(self):
        print("待つんだ")

class Else(IExpression):
    def Operate(self):
        print("よくわかりませんでした")

if __name__ == "__main__":
    main()