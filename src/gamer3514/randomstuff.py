import random
from datetime import datetime
from termcolor import colored
def hurricanecategory(speed):
    """
    Returns the category of a hurricane based on its wind speed.
    """
    if speed >= 157:
        category = "Five" 
    elif speed <= 130 or 156:
        category = "Four" 
    elif speed <= 111 or 129:
        category = "Three" 
    elif speed <= 96 or 110: 
        category = "Two"
    elif speed <= 74 or 95:
        category = "One"
    elif speed <= 73:
        category = "Windy"
    return category
def randomnumber():
    """
    Generate a random number between 0 and 999.
    """
    return random.randint(0, 999)
def screentime(hours):
    """
    Calculate the percentage of a day spent on a screen.
    """
    return hours / 24 * 100
def getpercentage(number, percentage):
    """
    Calculate the percentage of a number.
    """
    return number / 100 * percentage
def filespam(filepath,sentence,amount):
    """
    Spam a sentence in a file.
    """
    print("If this burns your computer, it's not my fault.\nSpamming...")
    sentence += "\n"
    f = open(filepath, "w")
    for i in range(amount):
        f.write(sentence)
    f.close()
    print("Done! Spamming complete. Rembember, if this burnt your computer, it's not my fault.")
def printspam(sentence,amount):
    """
    Spam a sentence in the console.
    """
    print("If this burns your computer, it's not my fault.\nSpamming...")
    for i in range(amount):
        print(sentence)
    print("Done! Spamming complete. Rembember, if this burnt your computer, it's not my fault.")
def niceprint(sentence):
    """
    Print a sentence with a nice format including time, date, and green coloring.
    """
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%d/%m/%Y")
    formatted_sentence = f"[{current_date} {current_time}] {sentence}"
    print(colored(formatted_sentence, 'green'))