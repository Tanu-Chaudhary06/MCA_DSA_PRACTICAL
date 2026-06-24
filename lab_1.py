from array import array

arr = array('i', [10, 20, 30, 40, 50])

i = int(input("Enter index: "))

base = arr.buffer_info()[0]

print("Element:", arr[i])
print("Address:", base + i * arr.itemsize)