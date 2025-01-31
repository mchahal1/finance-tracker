# Ask for monthly allowance and expenses in different categories
answer = 0
allowance = 0
food = 0
clothing = 0
entertainment = 0

allowance = input("whats ur allowance").int()
food = input("How much did you spend on food?").int()
clothing = input("How much did you spend on clothing?").int()
entertainment = input("How much did you spend on entertainment?").int()
# Calculate total expenses and remaining balance
allowance - food - clothing - entertainment = answer
print(answer)
# Display results
# Conditional message based on balance (depending on whether you overspent or underspent or spent just the right amount, write a specific message - try to be kind!)