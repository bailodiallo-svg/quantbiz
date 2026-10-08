print("================================")
print("        QUANTBIZ")
print("   Business Analytics Tool")
print("================================")

revenue = float(input("Enter your revenue (£): "))
expenses = float(input("Enter your expenses (£): "))
customers = int(input("Enter number of customers: "))

profit = revenue - expenses
revenue_per_customer = revenue / customers

marketing_spend = float(input("Enter your marketing spend (£): "))
new_customers = int(input("Enter number of new customers: "))

CAC= marketing_spend / new_customers

print("\n------ BUSINESS RESULTS ------")

print(f"Revenue: £{revenue:.2f}")
print(f"Expenses: £{expenses:.2f}")
print(f"Profit: £{profit:.2f}")
print(f"Revenue per Customer: £{revenue_per_customer:.2f}")
print(f"Customer Acquisition Cost: £{CAC:.2f}")

def calculate_profit(revenue,expenses):
    return revenue - expenses

profit_from_function = calculate_profit(revenue, expenses)
print(f"\nProfit calculated from function: £{profit_from_function:.2f}")

def calculate_profit_margin(profit, revenue):
    if revenue == 0:
        return None 
    else:
        return (profit / revenue) * 100

profit_margin_from_function = calculate_profit_margin(profit_from_function, revenue)

if profit_margin_from_function is not None:
    print(f"Profit Margin calculated from function: {profit_margin_from_function:.2f}%")
else:
    print("Profit Margin calculated from function: Undefined (Revenue is zero)")
