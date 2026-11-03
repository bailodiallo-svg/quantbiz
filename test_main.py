from main import (
    calculate_profit,
    calculate_profit_margin,
    calculate_CAC,
    calculate_revenue_per_customer,
)

print("\n------ TESTING calculate_profit ------")
assert calculate_profit(5000, 1800) == 3200
assert calculate_profit(1000, 1500) == -500
assert calculate_profit(0, 0) == 0

print("\n------ TESTING calculate_profit_margin ------")
assert calculate_profit_margin(3200, 5000) == 64.0
assert calculate_profit_margin(-500, 1000) == -50.0
assert calculate_profit_margin(0, 0) is None

print("\n------ TESTING calculate_CAC ------")
assert calculate_CAC(2000, 50) == 40.0
assert calculate_CAC(0, 10) == 0.0
assert calculate_CAC(1000, 0) is None

print("\n------ TESTING calculate_revenue_per_customer ------")
assert calculate_revenue_per_customer(5000, 100) == 50.0
assert calculate_revenue_per_customer(0, 10) == 0.0
assert calculate_revenue_per_customer(1000, 0) is None

print("\nAll tests passed successfully!")