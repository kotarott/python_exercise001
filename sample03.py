path = "test02.csv"

s = "new File"

with open(path, mode='w') as f:
    f.write(s)

ss = ["One", "Two", "Three"]

with open(path, "w") as f:
    f.writelines(ss)

with open(path, 'w') as f:
    f.write('\n'.join(ss))

# 作成のみ
with open('test03.csv', 'w'):
    pass

# ファイルが存在するとエラー、存在しない場合は新規作成
try:
    with open('test04.csv', 'x') as f:
        f.write(s)
except FileExistsError:
    pass

import os

if not os.path.isfile("test05.csv"):
    with open("test05.csv", "w") as f:
        f.write(s)
else:
    print('file exist')

# 最後に追記
with open(path, "a") as f:
    f.write("\nFour")

# その他
with open(path, "r+") as f:
    l = f.readlines()
    print(l)

with open(path, "w") as f:
    l.insert(0, "Zero\n")
    f.writelines(l)