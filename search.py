### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
source = ["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

# with open('source.csv', 'w', encoding="utf-8") as f:
#     f.writelines(','.join(source))

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く　1-2
    # if word in source:
    #     print("{}が見つかりした".format(word))
    # else:
    #     print("{}は存在しませんでした。検索リストについかします。".format(word))
    #     source.append(word)
    #     print(source)
    
    # 検索・追加（CSV）
    with open('source.csv', 'r', encoding='utf-8') as f:
        l = f.readline().rstrip().split(',')
    
    if word in l:
        print("{}が見つかりした".format(word))
    else:
        print("{}は存在しませんでした。検索リストについかします。".format(word))
        with open('source.csv', 'a') as f:
            f.write(',' + word)

if __name__ == "__main__":
    search()