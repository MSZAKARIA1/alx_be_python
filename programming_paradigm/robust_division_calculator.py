# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Convert arguments to float
        numerator = float(numerator)
        denominator = float(denominator)

        # Check if denominator is zero
        if denominator == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")

        # Perform division
        result = numerator / denominator
        return f"The result of the division is {result}"

    except ZeroDivisionError as e:
        return f"Error: {e}"

    except ValueError:
        return "Error: Please enter numeric values only."


