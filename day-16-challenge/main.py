from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine


def report(maker, machine):
    maker.report()
    machine.report()


def main():
    is_exit = False
    menu = Menu()
    maker = CoffeeMaker()
    machine = MoneyMachine()

    while not is_exit:
        print(f"What would you like? ({menu.get_items()})")
        choice = input()

        if choice == "off":
            break

        if choice == "report":
            report(maker, machine)
            continue
        else:
            current = menu.find_drink(choice)

            if current is None:
                print("Invalid choice!")
                continue

        print(f"Your order: {current.name}")

        if not maker.is_resource_sufficient(current):
            print("Sorry, we are out of resources.")
            continue

        machine.make_payment(current.cost)

        maker.make_coffee(current)

        report(maker, machine)

        print("Here is your {}. Enjoy!".format(choice))


main()

