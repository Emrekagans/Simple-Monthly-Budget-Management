# library
import numpy as np

# Income and expenditure data
monthly_salary = 39800
expenses = np.array([4957.5, 110, 20000, 1000, 2000]) # Expenditure categories (food, transportation, rent, entertainment, other)

# Expenditure categories names
categories = ['Food', 'Transportation', 'Rent', 'Entertainment', 'Other']

# Total spend
total_spend = np.sum(expenses)

# Savings calculation
savings = monthly_salary - total_spend

# How much was spent in which category
for i in range(len(categories)):
    print(f"{categories[i]} : {expenses[i]} TL")

# Most spent category
max_spending_index = np.argmax(expenses)
print(f"\nMost spent category : {categories[max_spending_index]}")

# Savings status
print(f"\nTotal spend : {total_spend} TL")
print(f"Monthly savings : {savings} TL")