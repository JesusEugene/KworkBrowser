"""
Text output with color
"""

from src.settings import DEBUG, ESCAPE_OUT


def print_debug_text(msg): #kek
    """print_debug_text(msh)
    
        This is function outputs text with debug color
    """
    if DEBUG:
        print("\033[35m{0}\033[0m".format(msg))

def print_warning_text(msg):
    """
    """
    if ESCAPE_OUT:
        print("\033[33m{0}\033[0m".format(msg))
    else:
        print(msg)

def print_good_text(msg):
    if ESCAPE_OUT:
        print("\033[32m{0}\033[0m".format(msg))
    else:
        print(msg)

def print_normal_text(msg):
    if ESCAPE_OUT:
        print("\033[33m{0}\033[0m".format(msg))
    else:
        print(msg)

def print_bad_text(msg):
    if ESCAPE_OUT:    
        print("\033[31m{0}\033[0m".format(msg))
    else:
        print(msg)