bakery_items = {"Bread":40, "Butter":120, "Jam":200, "Cheese":220, "Crossiant":60}
cart = {}
print("Welcome to the Shopping Cart Program!")

while True:
    print()
    print("Please type in one of these")
    print("1. View the item in Bakery")
    print("2. Add item ")
    print("3. View cart ")
    print("4. Remove Item ")
    print("5. compute total")
    print("6. exit program")

    select = int(input(" Type in a number to go on "))

    if select == 1:
        for key,value in bakery_items.items():
            print(key,':',value)

    if select == 2:
        item = input(" What would you like to add?  ")
        if item in bakery_items:
            cart[item]=bakery_items.get(item)
            print(f"'{item}' has been added to your cart.")
        else:
            print("Item in the Bakery")


    if select == 3:
        print("This is what is in your shopping cart")
        for item in cart:
            print(f"  {item} - ${cart[item]}")

    if select == 4:
        takeout = input(" Type in what you would like to remove?  ")
        if takeout in cart:
            cart.pop(takeout)
        else:
            print("Not in cart!")

    if select == 5:
        total = 0
        for item in cart:
            total += cart[item]
        print(f" ${total}")

    if select == 6:
        print("comeback soon.")
        break