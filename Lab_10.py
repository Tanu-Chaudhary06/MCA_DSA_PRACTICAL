#  queue operations

list = []

def enqueue():
    element = input("enter the element to be added:")
    list.append(element)
    print(list)

def dequeue():
    if list:
        element = list.remove(list[0])
        print(element)
