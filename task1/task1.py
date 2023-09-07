import pandas as pd


def find_in_csv(path ,x , y):
    data = pd.read_csv(path)  # path to csv файл
    print(data.iloc[x][y])

    return True

def find_in_json(path ,x , y):
    data = pd.read_json(path) # path to json файл
    print(data) #.iloc[x][y]

    return True

inc = list(input().split())
x, y, path = int(inc[0]), int(inc[1]), inc[2]
if path[-1] == 'v':
    find_in_csv(path, x, y)
else:
    find_in_json(path, x, y)

