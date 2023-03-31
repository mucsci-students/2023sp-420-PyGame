"""
This file is the main controller for the Spelling Bee Game
    - Run file through command line/terminal
    - Takes a single additional argument
    - Argument options:
        - No argument defaults to run GUI version
        - "--cli": runs the CLI version
        - "--test": runs the test controller
"""

def placeHolder():
    return

## call main menu for GUI
def main():
    import sys
    import os

    ## nt = windows
    if os.name!="nt": 
        sys.path.append(os.getcwd()+"/PyGame_Project/MVC")
        sys.path.append(os.getcwd()+"/PyGame_Project/Saves")
        sys.path.append(os.getcwd()+"/PyGame_Project/MVC/Controller")
        sys.path.append(os.getcwd()+"/PyGame_Project/MVC/Model")
        sys.path.append(os.getcwd()+"/PyGame_Project/MVC/Model/Saves")
        sys.path.append(os.getcwd()+"/PyGame_Project/MVC/Model/Database")
        sys.path.append(os.getcwd()+"/PyGame_Project/MVC/View_CLI")
        sys.path.append(os.getcwd()+"/PyGame_Project/MVC/View_GUI")  
    else:
        sys.path.append(os.getcwd()+"\\PyGame_Project\\MVC")
        sys.path.append(os.getcwd()+"\\PyGame_Project\\Saves")
        sys.path.append(os.getcwd()+"\\PyGame_Project\\MVC\\Controller")
        sys.path.append(os.getcwd()+"\\PyGame_Project\\MVC\\Model")
        sys.path.append(os.getcwd()+"\\PyGame_Project\\MVC\\Model\\Saves")
        sys.path.append(os.getcwd()+"\\PyGame_Project\\MVC\\Model\\Database")
        sys.path.append(os.getcwd()+"\\PyGame_Project\\MVC\\View_CLI")
        sys.path.append(os.getcwd()+"\\PyGame_Project\\MVC\\View_GUI")

    print(sys.path)

    from CLI_controller import main_menu_handler
    from gui_main_menu import start_gui

    ## list of passed paramaters
    passedValue = sys.argv
    
    if len(passedValue) > 1:
        if passedValue[1] == "--cli":
            main_menu_handler()
        if passedValue[1] == "--test":
            placeHolder()
    
    start_gui()

if __name__ == "__main__":
    main()