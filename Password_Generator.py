# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Create a list of random letters
random_letters = []
for i in range(0, nr_letters):
    random_letters.append(random.choice(letters))
# Create a list of random symbols
random_symbols = []
for i in range(0, nr_symbols):
    random_symbols.append(random.choice(symbols))
# Create a list of random numbers
random_numbers = []
for i in range(0, nr_numbers):
    random_numbers.append(random.choice(numbers))

# Concatenate the lists of random letters, symbols and numbers
random_list = random_letters + random_symbols + random_numbers
# Shuffle the list of random characters
random.shuffle(random_list)
# Convert the list of random characters to a string
random_string = ''.join(random_list)
print(f"Your password is: {random_string}")
