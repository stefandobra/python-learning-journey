def add_remove():
    list = []
        
    while True:
        print(f"The list is now {list}")
        step = input("a(d)d, (r)emove or e(x)it: ")
        if step.lower() == "d":
            item = len(list) + 1
            list.append(item)
        elif step.lower() == "r":
            list.pop(len(list) - 1)
        elif step.lower() == "x":
            print("Bye!")
            break
        else:
            continue


    return


add_remove()



