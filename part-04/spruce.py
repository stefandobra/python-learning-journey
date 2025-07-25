def spruce(height):
    spaces = height
    i = 1
    print("a spruce!")
    while i <= height:
        print(" " * (spaces - 1) + "*" * (2 * i - 1))
        i += 1
        spaces -= 1
    print(" " * (height - 1) + "*")



# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)