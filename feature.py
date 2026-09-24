def power (base, exponent):
    """ Arguments:
    base (int or float): The base number.
    exponent (int or float): The exponent to raise the base to.

    Returns:
    (int or float): The result of base raised to the power of exponent.
    """
    return base ** exponent

def fibonacci (n):
    """ Arguments:
    n (int): The position in the Fibonacci sequence.
    
    Returns: (int): The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else: 
        return fibonacci (n-1) + fibonacci (n - 2)


if __name__ == "__main__":
    print (power (2.5, 5))
    # print (power.__doc__)  
    
    for i in range (1, 6):
        print (fibonacci (i), end = ", ")
    print ("|")