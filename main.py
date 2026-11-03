def calculate_profit(revenue, expenses):
    return revenue - expenses


def calculate_profit_margin(profit, revenue):
    if revenue == 0:
        return None
    return (profit / revenue) * 100


def calculate_CAC(marketing_spend, new_customers):
    if new_customers == 0:
        return None
    return marketing_spend / new_customers


def calculate_revenue_per_customer(revenue, customers):
    if customers == 0:
        return None
    return revenue / customers

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


def get_non_negative_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter an integer value.")


def main():
    print("================================")
    print("        QUANTBIZ")
    print("   Business Analytics Tool")
    print("================================")

    # Collect inputs
    revenue = get_non_negative_float("Enter your revenue (£): ")
    expenses = get_non_negative_float("Enter your expenses (£): ")
    marketing_spend = get_non_negative_float("Enter marketing spend (£): ")
    customers = get_non_negative_int("Enter number of customers: ")
    new_customers = get_non_negative_int(
        "Enter number of new customers acquired: "
    )

    # Calculate profit
    profit = calculate_profit(revenue, expenses)

    # Display business results
    print("\n------ BUSINESS RESULTS ------")
    print(f"Revenue: £{revenue:.2f}")
    print(f"Expenses: £{expenses:.2f}")
    print(f"Profit: £{profit:.2f}")

    # Calculate profit margin
    profit_margin = calculate_profit_margin(profit, revenue)

    if profit_margin is not None:
        print(f"Profit Margin: {profit_margin:.2f}%")
    else:
        print("Profit Margin: Undefined (Revenue is zero)")

    # Calculate customer acquisition cost
    CAC = calculate_CAC(marketing_spend, new_customers)

    if CAC is not None:
        print(f"Customer Acquisition Cost: £{CAC:.2f}")
    else:
        print("Customer Acquisition Cost: Undefined (No new customers)")

    # Calculate revenue per customer
    revenue_per_customer = calculate_revenue_per_customer(
        revenue, customers
    )

    if revenue_per_customer is not None:
        print(f"Revenue per Customer: £{revenue_per_customer:.2f}")
    else:
        print("Revenue per Customer: Undefined (No customers)")


if __name__ == "__main__":
    main()
