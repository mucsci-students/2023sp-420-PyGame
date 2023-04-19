import sys 
from model_puzzle import *
from PIL import Image, ImageFont, ImageDraw 


def generateImage():
    puzzle = PuzzleStats()

    ## Load in card template
    my_image = Image.open("template.png")

    ## Load in Card Font
    cardFontT = ImageFont.truetype('SyneMono-Regular.ttf', 40)
    cardFontL = ImageFont.truetype('SyneMono-Regular.ttf', 80)
    cardFontS = ImageFont.truetype('SyneMono-Regular.ttf', 28)


    ## Prep image to have changes 
    image_editable = ImageDraw.Draw(my_image)

    ## Draw Card Title... PyGame Spelling Be: <Share Puzzle Key>
    title_text = "PyGame Spelling Bee: #######"
    image_editable.text((32,32), title_text, (00, 00, 00), font=cardFontT)



    #### ----------- Draw in Hex's (X,Y) ----------- ####

    ## -- Center (Three)
    image_editable.text((350,140), str(puzzle.shuffled_puzzle[1]), (00, 00, 00), font=cardFontL)

    image_editable.text((350,285), str(puzzle.shuffled_puzzle[0]), (00, 00, 00), font=cardFontL)

    image_editable.text((350,425), str(puzzle.shuffled_puzzle[2]), (00, 00, 00), font=cardFontL)

    ## -- Left Side (Two)
    image_editable.text((225,215), str(puzzle.shuffled_puzzle[3]), (00, 00, 00), font=cardFontL)

    image_editable.text((225,355), str(puzzle.shuffled_puzzle[4]), (00, 00, 00), font=cardFontL)

    ## -- Right Side (Two))
    image_editable.text((470,215), str(puzzle.shuffled_puzzle[5]), (00, 00, 00), font=cardFontL)

    image_editable.text((470,355), str(puzzle.shuffled_puzzle[6]), (00, 00, 00), font=cardFontL)



    #### ----------- Draw in Bot Box (X,Y) ----------- ####
    aaaaa_text = "\t Puzzle Rank: " + puzzle.get_rank()
    image_editable.text((40,600), aaaaa_text, (00, 00, 00), font=cardFontS)


    aaaaa_text = "\t Puzzle Score: " + puzzle.score + "/" + puzzle.total_points
    image_editable.text((40,640), aaaaa_text, (00, 00, 00), font=cardFontS)


    aaaaa_text = "\t Words Correct: " + len(puzzle.guesses) + "/" + len(puzzle.current_word_list)
    image_editable.text((40,680), aaaaa_text, (00, 00, 00), font=cardFontS)


    aaaaa_text = "\t High Score Rank: ######" 
    image_editable.text((40,720), aaaaa_text, (00, 00, 00), font=cardFontS)


    aaaaa_text = "\t #######"
    image_editable.text((40,760), aaaaa_text, (00, 00, 00), font=cardFontS)



    ## Save the new image 
    my_image.save("result.png")