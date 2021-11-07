# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the output in the following format.
# You can buy ___ apples and your change is ___ pesos.

# Function for entering the money you have and asking for the price of an apple
def get_money_and_apple_price():
    amount_money = float(input('The money you have: '))
    apple_price = float(input('How much is an apple? '))
    return amount_money, apple_price

# Function for computing and displaying the maximum number of apples and remaining money
def display_apples_and_change(amount_money, apple_price):
    apples = int(amount_money//apple_price)
    change = amount_money - (apples*apple_price)
    print(f'You can buy {apples} apples and your change is {change} pesos.')

# Variable for entering the money you have and asking for the price of an apple
money, apple = get_money_and_apple_price()
# Displaying the maximum apples and the remaining money
display_apples_and_change(money, apple)