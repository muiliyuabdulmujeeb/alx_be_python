user_monthly_income = float(input("Enter your monthly income:  "))
user_monthly_expenses = float(input("Enter your total monthly expenses:  "))

user_monthly_savings = user_monthly_income - user_monthly_expenses

projected_savings = (user_monthly_savings * 12) + (user_monthly_savings * 12 * 0.05)

print(f"Your monthly savings are ${int(user_monthly_savings)}.")
print(f"Projected savings after one year, with interest, is: ${int(projected_savings)}.")