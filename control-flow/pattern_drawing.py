size = int(input("Enter the size of your square pattern: \n"))
original_size = size
while size != 0:
    for i in range(original_size):
        print("*", end=" ")
    size -= 1
    print()
