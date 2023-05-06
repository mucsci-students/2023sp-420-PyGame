import os, sys, time, pytest

from PyGame_Project.MVC.Model.model_puzzle import *
from PyGame_Project.MVC.Model.imageGen import *
from PyGame_Project.MVC.Controller.controller_universal import *

pytest.fixture
def puzzleGen():
    PuzzleStats().clear()
    shareable_key = "csqkhzct"
    prep_game_from_share(shareable_key)

    
"""
Tests image share function, checks to see if a newly creaded PNG is made
"""
def test_share_imageGen():
    puzzleGen()

    ## makes list of everything in the current direcotry 
    oldDirectory = os.listdir(os.getcwd())

    generateImage()
    time.sleep(10)
    ## makes list of everything in the current direcotry, after the image is created 
    newDirectory = os.listdir(os.getcwd())

    check = False
    newFileCount = 0
    for file in newDirectory:
        ## finds if there is any new files in the current directory, after the imageGen function is called
        if not file in oldDirectory:
            ## Check if the new file is a PNG
            if ".png" in file.lower():
                newFileCount += 1
                check = True

    assert check and (newFileCount == 1)