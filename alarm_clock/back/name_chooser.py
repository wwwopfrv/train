import eel
from random import choice
NAMES = ['Alex', "Andrew", "Billow", "Richard"]

@eel.expose
def namess():
    return choice(NAMES)

