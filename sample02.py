path = "test01.csv"

# f = open(path)
# print(f.readline().split(',')[1])
# f.close()

with open(path) as f:
    # for row in f.readlines():
    #     print(row.rstrip().split(','))
    while True:
        row = f.readline()
        if not row:
            break
        print(row.rstrip().split(','))