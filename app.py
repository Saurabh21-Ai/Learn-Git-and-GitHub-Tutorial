def add (a, b):     # Addition function
    """Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of a and b.
    """
    return a + b

def factorial (n):     # Factorial function
    """Args:
        n (int): The number to calculate the factorial of.

    Returns:
        int: The factorial of n.
    """
    if n < 0:
        raise ValueError ("Factorial is not defined for negative numbers.")
    elif type(n) != int:
        raise TypeError ("Factorial is only defined for integers.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range (2, n + 1):
            result *= i
        return result


if __name__ == "__main__":
    print ("How are you?")
    print (add (5, 3))  # Example usage of the add function
    print (factorial (5))  
