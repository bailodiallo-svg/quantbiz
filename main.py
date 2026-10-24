print("================================")
print("        QUANTBIZ")
print("   Business Analytics Tool")
print("================================")

def get_non_negative_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

revenue = get_non_negative_float("Enter your revenue (£): ")
expenses = get_non_negative_float("Enter your expenses (£): ")
customers = get_non_negative_float("Enter number of customers: ")
marketing_spend = get_non_negative_float("Enter marketing spend (£): ")
new_customers = get_non_negative_float("Enter number of new customers acquired: ")

profit = revenue - expenses

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
