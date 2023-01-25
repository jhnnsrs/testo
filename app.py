
from arkitekt import register

@register()
def test_func(a: int, b: int, c: int) -> int:
    """Add three numbers



    This function adds two numbers and returns the result.

    Args:
        a (int): The first number
        b (int): The second number

    Returns:
        int: The returned number
    """
    return a + b + c

