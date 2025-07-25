def greatest_number(x,y,z):
    max = x
    if max < y:
        max = y
    if max < z:
        max = z
    return max


    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)