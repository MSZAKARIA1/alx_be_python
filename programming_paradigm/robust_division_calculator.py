# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Convert arguments to float
        numerator = float(numerator)
        denominator = float(denominator)

        # Check if denominator is zero
        if denominator == 0:
            # Handle division by zero with a custom message
            return "Error: Cannot divide by zero."

        # Perform division
        result = numerator / denominator
        return f"The result of the division is {result}"

    except ValueError:
        # Handle non-numeric input with a custom message
        return "Error: Please enter numeric values only."



