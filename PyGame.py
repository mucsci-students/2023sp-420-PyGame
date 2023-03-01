"""
This file is the main controller for the Spelling Bee Game
    - Run file through command line/terminal
    - Takes a single additional argument
    - Argument options:
        - No argument defaults to run GUI version
        - "--cli": runs the CLI version
        - "--test": runs the test controller
"""

import sys
import os

sys.path.append(os.getcwd()+"\\MVC\\Controller")
sys.path.append(os.getcwd()+"\\MVC\\Model")
sys.path.append(os.getcwd()+"\\MVC\\Model\\Database")
sys.path.append(os.getcwd()+"\\MVC\\View_CLI")

from CLI_controller import main_menu_handler


def placeHolder():
    return

## list of passed paramaters
passedValue = sys.argv

if len(passedValue) > 1:
    if passedValue[1] == "--cli":
        main_menu_handler()
    if passedValue[1] == "--test":
        placeHolder()

## call main menue for GUI
