print("================================")
print("        QUANTBIZ")
print("   Business Analytics Tool")
print("================================")

revenue = float(input("Enter your revenue (£): "))
expenses = float(input("Enter your expenses (£): "))
customers = int(input("Enter number of customers: "))

profit = revenue - expenses
profit_margin = (profit / revenue) * 100
revenue_per_customer = revenue / customers

marketing_spend = float(input("Enter your marketing spend (£): "))
new_customers = int(input("Enter number of new customers: "))

CAC= marketing_spend / new_customers

print("\n------ BUSINESS RESULTS ------")

print(f"Revenue: £{revenue:.2f}")
print(f"Expenses: £{expenses:.2f}")
print(f"Profit: £{profit:.2f}")
print(f"Profit Margin: {profit_margin:.2f}%")
print(f"Revenue per Customer: £{revenue_per_customer:.2f}")
print(f"Customer Acquisition Cost: £{CAC:.2f}")
