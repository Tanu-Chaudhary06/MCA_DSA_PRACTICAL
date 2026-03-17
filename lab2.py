#insert and delete an element at a given position in a list 

lst = [1,2,34,44,32]
print("original list",lst)

pos = int(input("Enter position to insert: "))
val = int(input("Enter value to insert: "))


if pos >= 0 and pos < len(lst):
    lst.insert(pos,val)
    print("list after insertion",lst)
else:
    print("invalid position")

#delete an element in list

pos = int(input("Enter position to delete: "))

if pos >= 0 and pos < len(lst):
    lst.pop(pos)
    print("list after deletion:",lst)
else:
    print("invalid position")

#search an element in a list

val = int(input("enter an element to search:"))

if val in lst:
    print("element found at index:",lst.index(val))
else:
    print("element not found.")

