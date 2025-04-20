# hotelmenu.py

# Hotel Menu Program

menu = {
    "1": {"item": "Idli", "price": 30},
    "2": {"item": "Dosa", "price": 50},
    "3": {"item": "Vada", "price": 20},
    "4": {"item": "Poori", "price": 40},
    "5": {"item": "Tea", "price": 10},
    "6": {"item": "Coffee", "price": 15}
}

def show_menu():
    print("\n--- HOTEL MENU ---")
    for key, value in menu.items():
        print(f"{key}. {value['item']} - ₹{value['price']}")
    print("0. Exit")

def take_order():
    total = 0
    order_list = []

    while True:
        show_menu()
        choice = input("Enter item number to order (0 to finish): ")

        if choice == "0":
            break
        elif choice in menu:
            qty = input(f"How many {menu[choice]['item']}s? ")
            if qty.isdigit():
                qty = int(qty)
                item_total = qty * menu[choice]['price']
                total += item_total
                order_list.append((menu[choice]['item'], qty, item_total))
                print(f"Added {qty} x {menu[choice]['item']} to order. Subtotal: ₹{item_total}")
            else:
                print("Invalid quantity. Please enter a number.")
        else:
            print("Invalid choice. Please select from the menu.")

    return order_list, total

def print_bill(order_list, total):
    print("\n--- BILL ---")
    for item, qty, item_total in order_list:
        print(f"{item} x {qty} = ₹{item_total}")
    print(f"Total Amount: ₹{total}")
    print("Thank you! Visit Again!")

# Main program
if __name__ == "__main__":
    orders, total_amount = take_order()
    if orders:
        print_bill(orders, total_amount)
    else:
        print("No items ordered. Goodbye!")
