def line(times, string):
    if string == "":
        string = "*"
    print(string[0] * times)

def box_of_hashes(height):
    i = 0
    while i < height:
        line(10, "#")
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
