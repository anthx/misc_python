def t(xs):
    return [[xs[i][j] for i in range(len(xs))] for j in range(len(xs[0]))]

y = t([[1,2,3],[4,5,6]])



from datetime import datetime
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))