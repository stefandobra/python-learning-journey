def invert(dictionary: dict):
    new_dict = {}
    for key in dictionary:
        new_dict[dictionary[key]] = key
    
    dictionary.clear()

    for key in new_dict:
        dictionary[key] = new_dict[key]
       
       
    
   
