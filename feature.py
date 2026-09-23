def power (base, exponent):
    """ Arguments:
    base (int or float): The base number.
    exponent (int or float): The exponent to raise the base to.

    Returns:
    (int or float): The result of base raised to the power of exponent.
    """
    return base ** exponent

if __name__ == "__main__":
    print (power (2.5, 5))
    print (power.__doc__)  