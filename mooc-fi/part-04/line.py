def line(times, string):
    if string == "":
        string = "*"
    print(string[0] * times)
    
    
    # if string == "":
    #     print("*" * times)
    # else:
    #     print(string[0] * times)



# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")
    line(7, "%")
    line(10, "LOL")
    line(3, "")