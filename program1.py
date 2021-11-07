# Create a program that will ask for name, age and address. 
# Display those details in the following format.
# Hi, my name is _____. I am ____ years old and I live in _____ .

# Function for input of name, age, address
def get_input():
    user_name = input('What is your name? ')
    user_age = int(input('How old are you? '))
    user_address = input('Where do you live? ')
    return user_name, user_age, user_address

# Function for displaying name, age, address
def display(user_name, user_age, user_address):
    print(f'Hi, my name is {user_name}. I am {user_age} years old and I live in {user_address}.')

# Variable for name, age, address
name, age, address = get_input()
# Variable for displaying name, age, address
display(name, age, address)