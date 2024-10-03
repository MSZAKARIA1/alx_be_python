def safe_divide(numerator, denominator):
    try:
        # Check if both numerator and denominator are numeric
        if not isinstance(numerator, (int, float)) or not isinstance(denominator, (int, float)):
            raise ValueError("Error: Please enter numeric values only.")

        # Check if the denominator is zero
        if denominator == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")

        # Perform the division
        result = numerator / denominator
        print(f"The result of the division is {result}")
        return result

    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Division attempt completed.")
