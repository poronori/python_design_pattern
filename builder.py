# 同じ生成過程で素材の異なるオブジェクトを作るパターンです。

def main():
    html = Director().construct(HTMLBuilder()) # HTMLで作成
    text = Director().construct(TextBuilder()) # テキストで作成
    
    print(html)
    print("-----------------------")
    print(text)

# builderクラスを集約する
class Director():
    def construct(self, builder):
        str = ""
        str += builder.build_title("休日の過ごし方")
        str += builder.build_header("------------")
        str += builder.build_contents(["朝起きる", "飯食う", "風呂入る", "寝る"])
        str += builder.build_footer("*==*=*==*==*==*")
        return str

# 抽象クラス
class Builder():
    def build_title(self, title):
        pass
    
    def build_header(self, header):
        pass
    
    def build_contents(self, contents):
        pass
    
    def build_footer(self, footer):
        pass

# HTMLクラス
class HTMLBuilder(Builder):
    def build_title(self, title):
        return "<h1>{}</h1>\n".format(title)
    
    def build_header(self, header):
        return "<header><p>{}</p></header>\n".format(header)
    
    def build_contents(self, contents):
        html = []
        for content in contents:
            html.append("<p>{}</p>\n".format(content))
        return "".join(html)
    
    def build_footer(self, footer):
        return "<footer><p>{}</p></footer>\n".format(footer)

# テキストクラス
class TextBuilder(Builder):
    def build_title(self, title):
        return "★★{}★★\n".format(title)
    
    def build_header(self, header):
        return "{}\n".format(header)
    
    def build_contents(self, contents):
        html = []
        for content in contents:
            html.append("{}\n".format(content))
        return "".join(html)
    
    def build_footer(self, footer):
        return "{}\n".format(footer)

if __name__ == "__main__":
    main()