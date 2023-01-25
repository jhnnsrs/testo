
from arkitekt import register

@register()
def test_func(a: int, b: int) -> int:
    """Add two numbers

    This function adds two numbers and returns the result.

    Args:
        a (int): The first number
        b (int): The second number

    Returns:
        int: The returned number
    """
    return a + b

