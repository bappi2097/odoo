MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def get_menu_list():
    return MENU.keys()

def validate_instruction(str):
    if str not in list(get_menu_list()) + ["report", "off"]:
        print("Invalid input. Please input from the list\n")
        return False
    return True

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}\n")

def check_availablity(coffee):
    available = True
    for res in MENU[coffee]["ingredients"]:
        if resources[res] < MENU[coffee]["ingredients"][res]:
            available = False
            print(f"Sorry there is not enough {res}.\n")
            break
    return available

def get_coin_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def total_price(quarters, dimes, nickles, pennies):
    return float(0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies)

def is_sufficient(quarters, dimes, nickles, pennies, coffee):
    total = total_price(quarters=quarters, dimes=dimes, nickles=nickles, pennies=pennies)
    return MENU[coffee]["cost"] <= total

def get_change(quarters, dimes, nickles, pennies, coffee):
    global profit, resources
    total = total_price(quarters=quarters, dimes=dimes, nickles=nickles, pennies=pennies)
    for res in MENU[coffee]["ingredients"]:
        resources[res] -= MENU[coffee]["ingredients"][res]
    profit += MENU[coffee]["cost"]
    return round(total - MENU[coffee]["cost"], 2)

if "__main__" == __name__:
    while True:
        try:
            instraction = input("What would you like? (espresso/latte/cappuccino):")
            if not validate_instruction(instraction):
                continue
            match instraction:
                case "espresso" | "latte" | "cappuccino":
                    if not check_availablity(instraction):
                        continue
                    print("Please insert coins.")
                    quarters = get_coin_input("How many quarters?:")
                    dimes = get_coin_input("How many dimes?:")
                    nickles = get_coin_input("How many nickles?:")
                    pennies = get_coin_input("How many pennies?:")
                    if not is_sufficient(quarters=quarters, dimes=dimes, nickles=nickles, pennies=pennies, coffee=instraction):
                        print("Sorry that's not enough money. Money refunded.\n")
                        continue
                    change = get_change(quarters=quarters, dimes=dimes, nickles=nickles, pennies=pennies, coffee=instraction)
                    if change != 0:
                        print(f"Here is ${change} in change.\n")
                    print(f"Here is your {instraction} Enjoy!\n")
                case "report":
                    report()
                case "off":
                    break
        except KeyboardInterrupt:
            break
        finally:
            print("\nShuting down....")