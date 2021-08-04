### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
source = ["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

# with open('source.csv', 'w', encoding="utf-8") as f:
#     f.writelines(','.join(source))

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    path = 'source.csv'
    ### ここに検索ロジックを書く　1-2
    # if word in source:
    #     print("{}が見つかりした".format(word))
    # else:
    #     print("{}は存在しませんでした。検索リストについかします。".format(word))
    #     source.append(word)
    #     print(source)
    
    # 検索・追加（CSV）
    nameList = readCSV(path, 'utf-8')
    
    if word in nameList:
        print("{}が見つかりした".format(word))
    else:
        print("{}は存在しませんでした。検索リストについかします。".format(word))
        writeCSV(path, word, 'utf-8')

### CSV読み込み
def readCSV(path, encodeType):
    with open(path, 'r', encoding=encodeType) as f:
        items = f.readline().rstrip().split(',')
    return items

### CSV書き込み
def writeCSV(path, item, encodeType):
    with open(path, 'a', encoding=encodeType) as f:
        f.write(',' + item)

if __name__ == "__main__":
    search()