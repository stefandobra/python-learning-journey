def chessboard(lenght):

    i = 0
    while i < lenght:
        if i % 2 == 0:
            row = "10" * lenght
        else:
            row = "01" * lenght

        print(row[0:lenght])
        i += 1

    # start = 1
    # one = "1"
    # zero = "0"
    # height = lenght
    # printed_rows = 0
    

    # while height > 0:
    #     row = ""
        
    #     while len(row) != lenght:
    #         if start == 1:
    #             row = row + one
    #             start -= 1
    #         else:
    #             row = row + zero
    #             start = 1

    #     height -= 1   
    #     print(row)
    #     printed_rows += 1
    #     if printed_rows %2 != 0:
    #         start = 0
    #     else:
    #         start = 1


# Testing the function
if __name__ == "__main__":
    chessboard(3)
    
    
    