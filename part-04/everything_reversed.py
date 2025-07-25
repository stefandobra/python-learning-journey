def everything_reversed(list: list):
    new_list = []
    for item in list:
        new_list.append(item[::-1])
    return new_list[::-1]
   
    
        

if __name__ == "__main__":
    # here the global variable is assigned
    name_list = ["Steve", "Jean", "Katherine", "Paul"]
    print(everything_reversed(name_list))
    print()
    print(everything_reversed(["Huey", "Dewey", "Louie"]))