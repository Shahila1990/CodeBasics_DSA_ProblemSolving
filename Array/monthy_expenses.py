expenses = {
    "January" : 2200,
    "February" : 2350,
    "March" : 2600,
    "April" : 2130,
    "May" : 2190
}

# 1. Extra in Feb compared to Jan
print("Extra in Feb compared to Jan :" , expenses["February"] - expenses["January"])

# 2. First quarter expenses
first_quarter_expenses = expenses["January"] + expenses["February"] + expenses["March"]
print("Total expenses of first quarter: " , first_quarter_expenses)

# 3. Did I spend 2000?
print("Did I spend 2000 in any month? " , "Yes" if 2000 in expenses.values() else "No")

# 4. Add June month expenses
expenses['June'] = 1980
print("After Adding June expenses: " , expenses)

# 5. Correction after refund
expenses["April"] = expenses["April"] -200
print("Expenses after the refund :" , expenses)