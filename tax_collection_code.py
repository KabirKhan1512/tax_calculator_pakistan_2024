# Tax system with multiple conditions based on yearly income.

# Input monthly income from the user
income = int(input("Enter your income for a month: "))

# Calculate yearly income by multiplying monthly income by 12
yearly_income = income * 12

# Check the yearly income and calculate the tax based on different tax brackets
if yearly_income > 600000 and yearly_income <= 1200000:
    # Tax for income between 600,000 and 1,200,000
    tax = (yearly_income - 600000) * 5/100
    category = "B"

elif yearly_income > 1200000 and yearly_income <= 2200000:
    # Tax for income between 1,200,000 and 2,200,000
    tax = (yearly_income - 1200000) * 15/100 + 30000
    category = "C"

elif yearly_income > 2200000 and yearly_income <= 3200000:
    # Tax for income between 2,200,000 and 3,200,000
    tax = (yearly_income - 2200000) * 25/100 + 180000
    category = "D"

elif yearly_income > 3200000 and yearly_income <= 4100000:
    # Tax for income between 3,200,000 and 4,100,000
    tax = (yearly_income - 3200000) * 30/100 + 430000
    category = "E"

elif yearly_income > 4100000:
    # Tax for income above 4,100,000
    tax = (yearly_income - 4100000) * 35/100 + 700000
    category = "F"

else:
    # No tax for income 600,000 or below
    tax = 0
    category = "A"

# Print the tax category and the tax amount for the current year
print(f"Your tax category is {category} and tax amount for one year is {tax}.")
