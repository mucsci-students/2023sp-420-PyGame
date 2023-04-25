import os 
from PyGame_Project.MVC.Model.model_puzzle import *
from PyGame_Project.MVC.Model.Database.model_highscores import *


from PIL import Image, ImageFont, ImageDraw 


def generateImage(saveName):
    puzzle = PuzzleStats()

    ## Load in card template

    image_dir = os.path.join(os.getcwd(), "PyGame_Project/MVC/Model")
    my_image = Image.open(os.path.join(image_dir, 'template.png'))

    ## Load in Card Font
    font_path = os.path.join(image_dir, 'SyneMono-Regular.ttf')
    cardFontT = ImageFont.truetype(font_path, 40)
    cardFontL = ImageFont.truetype(font_path, 80)
    cardFontS = ImageFont.truetype(font_path, 28)


    ## Prep image to have changes 
    image_editable = ImageDraw.Draw(my_image)

    ## Draw Card Title... PyGame Spelling Be: <Share Puzzle Key>
    title_text = "PyGame Spelling Bee: " + PuzzleStats().encode_puzzle_key().upper()
    image_editable.text((32,32), title_text, (64, 45, 24), font=cardFontT)



    #### ----------- Draw in Hex's (X,Y) ----------- ####

    ## -- Center (Three)
    image_editable.text((350,140), str(puzzle.shuffled_puzzle[1]).upper(), (64, 45, 24), font=cardFontL)

    image_editable.text((350,285), str(puzzle.shuffled_puzzle[0]).upper(), (64, 45, 24), font=cardFontL)

    image_editable.text((350,425), str(puzzle.shuffled_puzzle[2]).upper(), (64, 45, 24), font=cardFontL)

    ## -- Left Side (Two)
    image_editable.text((225,215), str(puzzle.shuffled_puzzle[3]).upper(), (64, 45, 24), font=cardFontL)

    image_editable.text((225,355), str(puzzle.shuffled_puzzle[4]).upper(), (64, 45, 24), font=cardFontL)

    ## -- Right Side (Two))
    image_editable.text((470,215), str(puzzle.shuffled_puzzle[5]).upper(), (64, 45, 24), font=cardFontL)

    image_editable.text((470,355), str(puzzle.shuffled_puzzle[6]).upper(), (64, 45, 24), font=cardFontL)



    #### ----------- Draw in Bot Box (X,Y) ----------- ####
    aaaaa_text = "\t Puzzle Rank: " + puzzle.get_rank()
    image_editable.text((40,600), aaaaa_text, (64, 45, 24), font=cardFontS)


    aaaaa_text = "\t Puzzle Score: " + str(puzzle.score) + "/" + str(puzzle.total_points)
    image_editable.text((40,640), aaaaa_text, (64, 45, 24), font=cardFontS)


    aaaaa_text = "\t Words Correct: " + str(len(puzzle.guesses)) + "/" + str(len(puzzle.current_word_list))
    image_editable.text((40,680), aaaaa_text, (64, 45, 24), font=cardFontS)
    
    ##def get_player_rank(player_name, required_letter, all_letters):
    playerRank = get_player_rank(saveName, puzzle.required_letter, puzzle.pangram)

    aaaaa_text = "\t High Score Rank: " + str(playerRank[2]) + "/" + str(playerRank[3])  
    image_editable.text((40,720), aaaaa_text, (64, 45, 24), font=cardFontS)

    """ 
    aaaaa_text = "\t #######"
    image_editable.text((40,760), aaaaa_text, (64, 45, 24), font=cardFontS)
    """


    ## Save the new image 
    my_image.save(os.path.join(os.getcwd(), saveName + ".png"))