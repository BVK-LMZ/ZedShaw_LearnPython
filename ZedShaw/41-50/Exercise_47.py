# ZedShaw Python Exercise #47
# This Exercise is all about... AUTOMATED TESTING


def calculate_discount(amount):
    """
    Calculate 25% discount off a given purchase amount.

    Args:
    - amount (float): The purchase amount before discount.

    Returns:
    - float: The discounted amount after applying a 25% discount.
    """
    discount_rate = 0.25  # 25% discount
    discount = amount * discount_rate
    discounted_amount = amount - discount
    return discounted_amount


def RunTest():
    """
    Run test cases for calculate_discount function and return Pass or Fail based on results.
    """
    test_cases = [
        (100.0, 75.0),  # Test case: 25% off $100 = $75
        (200.0, 150.0),  # Test case: 25% off $200 = $150
        # Add more test cases as needed
        #(150.0, 120.0)    # Expected: 25% off $150 = $112.5, but actual: $120.0
    ]

    checks = []

    for amount, expected_discounted_amount in test_cases:
        actual_discounted_amount = calculate_discount(amount)
        check = actual_discounted_amount == expected_discounted_amount
        checks.append(check)

    if all(checks):
        return "Pass"
    else:
        return "Fail"

# Example usage (optional)
if __name__ == "__main__":
    result = RunTest()
    print(f"Test result: {result}")
