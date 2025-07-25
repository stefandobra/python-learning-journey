def list_of_stars(list: list):
    for number in list:
        print("*" * number)

if __name__ == "__main__":
    list_of_stars([1,2,3,4,4,4,5,6,7])