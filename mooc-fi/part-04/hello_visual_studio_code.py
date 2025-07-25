def editor():
    while True:
        editor_name = input("Editor: ").lower()
        if editor_name == "visual studio code":
            print("an excellent choice!")
            break
        elif editor_name == "word" or editor_name == "notepad":
            print("awful")
        else:
            print("not good")



editor()