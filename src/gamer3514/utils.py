import random
def randomnumber():
    """
    Generate a random number between 0 and 999.
    """
    return random.randint(0, 999)
def genpassword(length):
    """
    Generate a random password.
    """
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()_+-=[]{};:,./<>?"
    password = ""
    while len(password) != length:
        randomnumber = random.randint(0, 2)
        if randomnumber == 0:
            password += random.choice(letters)
        elif randomnumber == 1:
            password += random.choice(numbers)
        elif randomnumber == 2:
            password += random.choice(symbols)
    return password 
