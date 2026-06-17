# Project 2: EXPENSE TRACKER

# Initialize the accumulator to 0
total_expenses = 0.0

print("Welcome to the Expense Tracker!")
print("Type 'done' when you are finished adding expenses.\n")

# Loop to keep asking the user for expense amounts
while True:
    # Get user input
    user_input = input("Enter an expense amount: ")
    
    # Check if the user wants to stop
    if user_input.lower() == 'done':
        break
    
    try:
        # Convert the input string to a float (decimal number)
        amount = float(user_input)
        
        # Accumulator: add the new amount to the total
        total_expenses += amount
        
        # Show the current running total
        print(f"Added! Current total: ${total_expenses:.2f}\n")
    except ValueError:
        print("Invalid input. Please enter a valid number or 'done'.\n")

# Display the final total
print("----------------------------------")
print(f"Your total expenses are: ${total_expenses:.2f}")
