# Simple Calculator in Python
# This program lets you add, subtract, multiply, or divide two numbers.

# First, we create "functions".
# A function is just a mini-program we can reuse.
# Example: instead of writing x + y every time, we make a function called add().

def add(x, y):   # This function takes 2 numbers (x and y)
    return x + y # It gives back (returns) the sum of those 2 numbers

def subtract(x, y):       # Function for subtraction
    return x - y          # It returns the difference (x minus y)

def multiply(x, y):       # Function for multiplication
    return x * y          # It returns the product (x times y)

def divide(x, y):         # Function for division
    return x / y          # It returns the quotient (x divided by y)

# Now let’s guide the user on what they can do.
print("Select operation:")   # This prints a title
print("1. Add")              # Option 1 is Addition
print("2. Subtract")         # Option 2 is Subtraction
print("3. Multiply")         # Option 3 is Multiplication
print("4. Divide")           # Option 4 is Division

# Let’s ask the user to choose.
choice = input("Enter choice (1/2/3/4): ")
# input() waits for the user to type something on the keyboard.
# Whatever they type is stored in the variable 'choice'.

# Now let’s ask for the actual numbers.
num1 = float(input("Enter first number: "))   # we change the input to float, so math works
num2 = float(input("Enter second number: "))  # same here, both numbers are now real numbers

# Now comes the "decision making" part.
# We use IF and ELSE to check what the user chose.

if choice == '1':   # If the user typed 1
    print("Result:", add(num1, num2))  # We call the add() function

elif choice == '2': # If they typed 2
    print("Result:", subtract(num1, num2))  # We call the subtract() function

elif choice == '3': # If they typed 3
    print("Result:", multiply(num1, num2))  # We call the multiply() function

elif choice == '4': # If they typed 4
    # Before dividing, check if the second number is zero
    if num2 == 0:   # Dividing by zero is impossible
        print("Error! Division by zero is not allowed.")
    else:
        print("Result:", divide(num1, num2))  # Safe to divide

else:
    # If the user typed something other than 1/2/3/4
    print("Invalid input")
