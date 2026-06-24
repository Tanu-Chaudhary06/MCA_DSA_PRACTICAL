# find the maximum element in an array

arr = [10, 25, 5, 40, 15]

max_val = arr[0]

for i in arr:
    if i > max_val:
        max_val = i

print("Maximum element is:", max_val)