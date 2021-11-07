# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format.
# The total amount is ______.

# Function for asking how many apples and oranges you want to buy
def get_apples_and_oranges():
    apple_count = int(input('The price of an apple is 20 pesos. How many apples you want to buy? '))
    orange_count = int(input('The price of an orange is 25 pesos. How many oranges you want to buy? '))
    return apple_count, orange_count

# Function for computing and displaying the total
def display_total(apple_count, orange_count):
    total= (apple_count*20) + (orange_count*25)
    print(f'The total amount is {total}')

# Variable for input of apples and oranges
apples, oranges = get_apples_and_oranges()
# Variable for displaying the total amount
display_total(apples, oranges)