"""
Coffee Machine Simulator
Author: Ramathatchana M
Description: A command-line coffee machine that manages resources, handles payments, and processes orders using loops and functions.
"""
water_ini=300
milk_ini=200
coffee_ini=100
money_ini=0.0

def calculate_money():
    print("Please insert coins.")
    q = int(input("How many quarters?: "))
    d = int(input("How many dimes?: "))
    n = int(input("How many nickels?: "))
    p = int(input("How many pennies?: "))
    return q*0.25 + d*0.10 + n*0.05 + p*0.01
  
while True:
    need=input("What would you like? (espresso/latte/cappuccino/report/off): ").strip().lower()
    if need == "off":
        print("Turning off machine.")
        break
    if need=="report":
        print("Milk : ",milk_ini)
        print("Coffee : ",coffee_ini)
        print("Money : ",money_ini)
    else:
        if need=="latte":
            if water_ini<200:
                print("Sorry there is not enough water.")
                continue
            elif milk_ini<150:
                print("Sorry there is not enough milk.")
                continue
            elif coffee_ini<24:
                print("Sorry there is not enough coffee.")
                continue
            total=calculate_money()
            rem = total - 2.50
            if rem>=0:
                print(f"Here is ${round(rem,2)} in change.")
                print("Here is your latte Enjoy!")
                money_ini += 2.50
                water_ini -= 200
                milk_ini  -= 150
                coffee_ini-= 24
            else:
                print("Sorry that's not enough pennies. Money refunded.")
        
        elif need=="espresso":
            if water_ini<50:
                print("Sorry there is not enough water.")
                continue
            elif coffee_ini<18:
                print("Sorry there is not enough coffee.")
                continue
            total=calculate_money()
            rem = total - 1.50
            if rem>=0:
                print(f"Here is ${round(rem,2)} in change.")
                print("Here is your espresso Enjoy!")
                money_ini += 1.50
                water_ini -= 50
                milk_ini  -= 0
                coffee_ini-= 18
            else:
                print("Sorry that's not enough pennies. Money refunded.")

        elif need=="cappuccino":
            if water_ini<250:
                print("Sorry there is not enough water.")
                continue
            elif milk_ini<100:
                print("Sorry there is not enough milk.")
                continue
            elif coffee_ini<24:
                print("Sorry there is not enough coffee.")
                continue
            total=calculate_money()
            rem = total - 3.00
            if rem>=0:
                print(f"Here is ${round(rem,2)} in change.")
                print("Here is your cappuccino Enjoy!")
                money_ini += 3.00
                water_ini -= 250
                milk_ini  -= 100
                coffee_ini-= 24 
            else:
                print("Sorry that's not enough pennies. Money refunded.")
        else:
              print("Invalid selection. Please choose a valid option.")
