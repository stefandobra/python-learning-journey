def line(times, string):
    if string == "":
        string = "*"
    print(string[0] * times)

def square_of_hashes(size):
    i = 0
    while i < size:
        line(size, "#")
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
