def mult_by_factor(value: int, factor: int = 1) -> int:
    """
    Multiply a value by a given factor.

    Args:
        value (int): The value to be multiplied.
        factor (int, optional): The factor to multiply the value by. Defaults to 1.

    Returns:
        int: The result of multiplying the value by the factor.
    """
    return value * factor


mult_by_factor(10)
mult_by_factor(10, 5)


def divide_by(value: float, devider: int = 1) -> float:
    return value / devider


value = input("Enter a value: ")
print("You entered:", value)
print("Result:", mult_by_factor(value))
