import csv

with open('strikes.csv', 'r', encoding='utf-8') as f:
    data = [list(map(int, row)) for row in csv.reader(f, delimiter='\t')]

cols = len(data[0]) if len(data) > 0 else 0
result = [[0.0 for _ in range(cols)] for _ in range(len(data))]


def count_neighbors(matrix, i, j):
    count, cells = 0, 0
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di == 0 and dj == 0:
                continue
            ni, nj = i + di, j + dj
            if 0 <= ni < len(data) and 0 <= nj < cols:
                count += matrix[ni][nj]
                cells += 1
    return count, cells


with open('predict.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    for i in range(len(data)):
        for j in range(cols):
            count, cells = count_neighbors(data, i, j)
            probability = count / cells if cells > 0 else 0.0
            if data[i][j] == 1:
                probability = max(0.0, probability - 0.1)
            result[i][j] = round(probability, 3)
        writer.writerow(result[i])