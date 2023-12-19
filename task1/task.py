import pandas as pd


def task(path, x, y):
    if path[-3:] == 'csv':
        data = pd.read_csv(path)  # path to csv файл
        print(data.iloc[x][y])
    else:
        data = pd.read_json(path)  # path to json файл
        print(data.iloc[x][y])  # .iloc[x][y]
    return True


inc = list(input().split())

task(inc[0], int(inc[1]), int(inc[2]))
