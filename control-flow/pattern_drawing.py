size = int(input("Enter the size of the pattern:"))
original_size = size
while size != 0:
    for i in range(original_size):
        print("*", end="")
    size -= 1
    print()
