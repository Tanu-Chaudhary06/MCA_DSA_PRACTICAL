data = [23,233,45,67,89]

for i in range(len(data)):
    min = i

    for j in range(i+1, len(data)):
        if data[j] < data[min]:
            min = j
    data[i], data[min] = data[min], data[i]
    print(data)