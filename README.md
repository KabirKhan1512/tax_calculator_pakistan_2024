

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
