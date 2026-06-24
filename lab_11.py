matrix = [[1, 2, 3], 
          [4, 5, 6],
            [7, 8, 9]]

rows = 3
cols = 3

print("Row major order")
for i in range(rows):
    for j in range(cols):
        print(matrix[i] [j],end=' ')
    print()

# for column major order
print("\nColumn-major order")
for j in range(cols):
    for i in range(rows):
        print(matrix[i][j],end=' ')
    print()
