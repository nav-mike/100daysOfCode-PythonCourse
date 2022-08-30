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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

COINS = {
    'quarters': 0.25,
    'dimes': 0.10,
    'nickels': 0.05,
    'pennies': 0.01,
}


def report(money):
    for item in resources.keys():
        print("{}: {}".format(item, resources[item]))
    print("Money: {}".format(money))


def decrease_resources(current, ingredient):
    resources[ingredient] -= current['ingredients'][ingredient]


def is_enough_resources(current):
    for item in resources.keys():
        if current['ingredients'][item] > resources[item]:
            print("Sorry there is not enough {}.", item)
            return False
    return True


def default_coins():
    return {'quarters': 0, 'dimes': 0, 'nickels': 0, 'pennies': 0}


def grab_coins():
    coins = default_coins()
    coin = input("Pass coins to the machine (quarters/dimes/nickles/pennies/_end):")
    while coin != "_end":
        if coin in COINS:
            coins[coin] += 1
        else:
            print("Invalid coin!")
        coin = input()
    return coins


def main():
    money = 0.0

    while True:
        choice = input("What would you like? (espresso/latte/cappuccino)")

        if choice == "off":
            break

        if choice in MENU:
            current = MENU[choice]
        elif choice == "report":
            report(money)
            continue
        else:
            print("Invalid choice!")
            continue

        print("Your order: {}".format(choice))

        if not is_enough_resources(current):
            continue

        coins = grab_coins()

        total = 0.0
        for coin in COINS:
            if coins[coin] > 0:
                total += COINS[coin] * coins[coin]

        print(f"Total: {total:.2g}")

        if total < current['cost']:
            print("Sorry, that's not enough money. Money refunded.")
            continue

        if total > current['cost']:
            change = total - current['cost']
            total -= change
            print(f"Here is {change:.2g} in  change")

        money += total

        for item in resources.keys():
            decrease_resources(current, item)

        report(money)

        print("Here is your {} ☕️. Enjoy!".format(choice))


main()
