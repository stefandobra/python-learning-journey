def squared(string, times):
    i = 0
    row =""
    lenght = len(string)
    

    while i < times * times:
        
        
        if i > 0 and i % times == 0:
            print(row)
            row = ""
        row += string[i % lenght]
        i += 1
    print(row)


    


# Testing the function
if __name__ == "__main__":
    squared("python", 15)
    # squared("ab", 3)
    #squared("aybabtu", 5)
    # squared("abcd", 4)




    
    # lenght = len(string)
    # row = string
    # rows = 0
    # repeat = (times // lenght + 1)


    # while rows < times:
    #     if lenght > times:
    #         row = string[0:times]
    #         string = string[times:] + row
    #         print(row)
            
    #     elif lenght < times:
    #         row = string * repeat
    #         row = row[0:times]
    #         string = row[times-lenght:]
    #         print(row)
    #     else:
    #         print(row)
    #     rows += 1
        


    

