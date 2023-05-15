MENU = {
    'sandwich': 10,
    'tea': 7,
    'salad': 8,
    'pizza': 12,
    'soup': 6
}


def interact_with_customer():
    total = 0

    while True:
        order = input("Order: ").lower().strip()

        if order == "":
            print("Your total is", total)
            break

        if order in MENU:
            price = MENU[order]
            total += price
            print(f"{order} costs {price}, total is {total}")
        else:
            print("Sorry, we don't have", order, "today.")


interact_with_customer()