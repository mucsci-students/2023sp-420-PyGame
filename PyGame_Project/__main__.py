"""
This file is the main controller for the Spelling Bee Game
    - Run file through command line/terminal
    - Takes a single additional argument
    - Argument options:
        - No argument defaults to run GUI version
        - "--cli": runs the CLI version
"""



## call main menu for GUI
def main():
    import sys
    import os
    from PyGame_Project.MVC.Controller.CLI_controller import main_menu_handler
    from PyGame_Project.MVC.View_GUI.gui_main_menu import start_gui

    ## list of passed paramaters
    passedValue = sys.argv
    
    if len(passedValue) > 1:
        if passedValue[1] == "--cli":
            main_menu_handler()

    
    start_gui()

if __name__ == "__main__":
    main()