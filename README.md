

## Tax System with Multiple Conditions Based on Yearly Income

This script calculates the yearly tax based on the user's monthly income according to specified tax brackets. The tax brackets and corresponding tax rates are applied to different ranges of yearly income.

### How to Use

1. **Input Monthly Income:**
   - The script prompts the user to enter their monthly income.
   - Example: `Enter your income for a month: 50000`

2. **Calculate Yearly Income:**
   - The script multiplies the monthly income by 12 to calculate the yearly income.
   - Example: If the monthly income is 50,000, the yearly income is `50,000 * 12 = 600,000`.

3. **Tax Calculation Based on Yearly Income:**
   - The script checks the yearly income and calculates the tax based on the following tax brackets:
     - **Category A:** Yearly income ≤ 600,000
       - Tax: 0
     - **Category B:** 600,001 < Yearly income ≤ 1,200,000
       - Tax: 5% of income exceeding 600,000
     - **Category C:** 1,200,001 < Yearly income ≤ 2,200,000
       - Tax: 15% of income exceeding 1,200,000 + 30,000
     - **Category D:** 2,200,001 < Yearly income ≤ 3,200,000
       - Tax: 25% of income exceeding 2,200,000 + 180,000
     - **Category E:** 3,200,001 < Yearly income ≤ 4,100,000
       - Tax: 30% of income exceeding 3,200,000 + 430,000
     - **Category F:** Yearly income > 4,100,000
       - Tax: 35% of income exceeding 4,100,000 + 700,000

4. **Output:**
   - The script prints the tax category and the tax amount for one year.
   - Example Output: `Your tax category is B and tax amount for one year is 50,000.`

### Example Usage

```python
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
```

