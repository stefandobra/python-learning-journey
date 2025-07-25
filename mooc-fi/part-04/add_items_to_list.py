def add_items(list):
    items = int(input("how many items: "))
    
    while len(list) < items:
        item = int(input(f"Item {len(list) + 1}: "))
        list.append(item)
        
    return list


list = []
add_items(list)
print(list)

