print("================================")
print("        QUANTBIZ")
print("   Business Analytics Tool")
print("================================")

try:
    revenue = float(input("Enter your revenue (£): "))
except ValueError:
    print("Invalid input for revenue. Please enter a numeric value.")
    exit(1)

if revenue < 0:
    print("Revenue cannot be negative. Please enter a valid amount.")
    exit(1)

try:
    expenses = float(input("Enter your expenses (£): "))
except ValueError:
    print("Invalid input for expenses. Please enter a numeric value.")
    exit(1)

if expenses < 0:
    print("Expenses cannot be negative. Please enter a valid amount.")
    exit(1)

try:
    customers = int(input("Enter number of customers: "))
except ValueError:
    print("Invalid input for customers. Please enter a whole number.")
    exit(1)

if customers < 0:   
    print("Number of customers cannot be negative. Please enter a valid number.")
    exit(1)

profit = revenue - expenses

try:
    marketing_spend = float(input("Enter marketing spend (£): "))
except ValueError:
    print("Invalid input for marketing spend. Please enter a numeric value.")
    exit(1)

if marketing_spend < 0:
    print("Marketing spend cannot be negative. Please enter a valid amount.")
    exit(1)

try:
    new_customers = int(input("Enter number of new customers acquired: "))
except ValueError:
    print("Invalid input for new customers. Please enter a whole number.")
    exit(1)

if new_customers < 0:
    print("Number of new customers cannot be negative. Please enter a valid number.")
    exit(1)


print("\n------ BUSINESS RESULTS ------")

print(f"Revenue: £{revenue:.2f}")
print(f"Expenses: £{expenses:.2f}")
print(f"Profit: £{profit:.2f}")

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

def calculate_CAC(marketing_spend, new_customers):
    if new_customers == 0:
        return None 
    else:
        return marketing_spend / new_customers

CAC_from_function = calculate_CAC(marketing_spend, new_customers)

if CAC_from_function is not None:
    print(f"Customer Acquisition Cost calculated from function: £{CAC_from_function:.2f}")
else:
    print("Customer Acquisition Cost calculated from function: Undefined (No new customers)")

def calcualate_revenue_per_customer(revenue, customers):
    if customers == 0:
        return None 
    else:
        return revenue / customers

revenue_per_customer_from_function = calcualate_revenue_per_customer(revenue, customers)

if revenue_per_customer_from_function is not None:
    print(f"Revenue per Customer calculated from function: £{revenue_per_customer_from_function:.2f}")
else:
    print("Revenue per Customer calculated from function: Undefined (No customers)")
