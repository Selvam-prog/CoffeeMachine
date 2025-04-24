""" MENU  is a dictionary that consists of all the menu items. Each of the menu item
consists of a dictionary that shows the ingredients as one of the keys and its value is again a dictionary
and cost as another key-value pair"""
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0,
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

"""resources is a dictionary that consists of three key-value pairs"""
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#loop_through is a global variable which determines the continuity of the loop
loop_through = True

#Below are the values of different coins
quarters = 0.25
dimes = 0.10
nickle = 0.05
pennies = 0.01

#global variable which gets updated after every usage of the machine.
amt_mach = 0


#function that calculates the total amount given by the user
def calculate (qcount,dcount,ncount,pcount):
    dollar = 0
    dollar = 0.25 * qcount + 0.10 * dcount + 0.05 * ncount + 0.01 * pcount
    return dollar

#function that checks if the available resource in the machine is sufficient to make coffee
def  is_resources_sufficient(user_wish):
    global loop_through
    water = resources["water"]
    milk = resources["milk"]
    coffee= resources["coffee"]

    if user_wish == 'report':
        print(f" Water:{water}\n Milk: {milk} \n Coffee: {coffee} \n Money: {amt_mach}\n")
        return

    else:
        if water >= MENU[user_wish]["ingredients"]["water"]:
            if milk >= MENU[user_wish]["ingredients"]["milk"]:
                if coffee >= MENU[user_wish]["ingredients"]["coffee"]:
                    resources ["water"] -= MENU[user_wish]["ingredients"]["water"]
                    resources["milk"] -= MENU[user_wish]["ingredients"]["milk"]
                    resources["coffee"] -= MENU[user_wish]["ingredients"]["coffee"]
                    return True
        else:
            print("Resources are insufficient . Sorry!")
            return False

#function that checks for the correct amount and delivers the coffee
def is_sufficient_amount(value, user_wish):

    global amt_mach
    cost = MENU [user_wish]["cost"]

    if value == cost:
        print(f"Here is your balance amount: ${value}")
        print(f"Here is your {user_wish} . Enjoy!")
        amt_mach += cost
        return True
    elif value > cost:
        value = value - cost
        value = round(value,2)
        print(f"Here is your balance amount: ${value}")
        print(f"Here is your {user_wish} . Enjoy!")
        amt_mach += cost
        return True
    else:
        print(f"Sorry, your amount is less than needed.Money refunded !")
        return False


while loop_through:
    amount = 0
    user_wish = input("What would you like? (espresso/latte/cappuccino)").lower()

    if user_wish not in MENU and user_wish!= 'off' and  user_wish!= 'report':
        print("Kindly give any one of valid options :latte /espresso/cappuccino")
        print("\n\n")


    elif user_wish == 'off':
        loop_through = False


    elif user_wish == 'report':
        is_resources_sufficient(user_wish)


    else:
        print(f"The cost of your favourite {user_wish} is : ${MENU[user_wish]['cost']}")
        print("Please insert coins.")
        q_count = int(input("how many quarters?:"))
        d_count = int(input("how many dimes?:"))
        n_count = int(input("how many nickles?:"))
        p_count = int(input("how many pennies?:"))
        amount = calculate(q_count,d_count,n_count,p_count)
        if is_resources_sufficient(user_wish):
            is_sufficient_amount(amount, user_wish)










