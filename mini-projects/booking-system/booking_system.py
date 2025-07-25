def add_booking(bookings: list):
    name = input("Customer name: ")
    date = input("Date (DD-MM-YYYY): ")
    treatment = input("Treatment required: ")
    bookings.append(f"{name} on {date} with {treatment}")
    print(f"✅ Booking for {name} added.\n")

def view_bookings(bookings: list):
    if not bookings:
        print("No bookings yet.\n")
        return
    i = 0
    while i < len(bookings):
        print(f"{i+1}. {bookings[i]}")
        i += 1
    print()

def cancel_booking(bookings: list):
    view_bookings(bookings)
    index = int(input("Please select booking to cancel: "))
    print()
    if index > len(bookings):
        print("Invalid selection\n")
        return
    
    bookings.pop(index - 1)

def run_menu():
    bookings = []
    while True:
        print("1. Add Booking\n2. View Bookings\n3. Cancel Booking\n0. Exit\n")
        choice = input("Please choose option: ")
        print()
        if choice == "1":
            add_booking(bookings)
        elif choice == "2":
            view_bookings(bookings)
        elif choice == "3":
            cancel_booking(bookings)
        elif choice == "0":
            break
        else:
            print("Invalid selection\n")
    print("Goodbye!")

run_menu()







