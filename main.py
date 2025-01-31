# Ask for monthly allowance and expenses in different categories

answer = 0
allowance = 0
food = 0
clothing = 0
entertainment = 0

allowance = int(input("whats ur allowance"))
food = int(input("How much did you spend on food?"))
clothing = int(input("How much did you spend on clothing?"))
entertainment = int(input("How much did you spend on entertainment?"))
# Calculate total expenses and remaining balance
answer = allowance - food - clothing - entertainment

# Display results
print("Here's your balance:")
print(answer)

# Conditional message based on balance (depending on whether you overspent or underspent or spent just the right amount, write a specific message - try to be kind!)
if answer > 0:
    print("Good spending!")
if answer == 0:
    print("Juuust right. No more money left!")
if answer < 0:
    print("tough, cant be spending THAT much.")