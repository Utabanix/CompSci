import time
import os
import sys

# Function to clear the console
def clear_console():
    if os.name == 'nt':  
        # For Windows
        os.system('cls')
    else:  
        # For macOS and Linux
        os.system('clear')

clear_console()

# Welcome message
print("\n**FACTORIAL FINDER BY UTABANIX**\n")

# Function to restart the program
def restart_program():
    print("Action not recognized\nRestarting Program...")
    time.sleep(5)
    os.execl(sys.executable, sys.executable, *sys.argv)

# Function to ask if the user wants to quit or run another calculation
def ask_to_continue():
    choice = input("\nDo you want to quit the script or run another calculation?\n(q to quit / any other key to restart): ")
    if choice.lower() == 'q':
        print("Quitting the script...")
        time.sleep(3)
        sys.exit()
    else:
        print("\nRestarting the script...")
        time.sleep(3)
        os.execl(sys.executable, sys.executable, *sys.argv)

# Function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Function to validate numerical input and restart program if not valid
def is_valid_number(value):
    return value.isdigit() and int(value) >= 0

# Main program
value = input("Enter a non-negative integer to find its factorial: ")
print()

if is_valid_number(value):
    value = int(value)
    result = factorial(value)
    print(f"The factorial of {value} is {result}")
else:
    restart_program()

# Asks if the user wants to run the script again or quit
ask_to_continue()