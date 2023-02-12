import unittest
import Output
import io
import sys
import os

#UNIT TEST CLASS FOR THE OUTPUT.PY FILE.
class TestSpellingBeeOutput(unittest.TestCase):

    # Unit test for the print_start_screen method
    def test_print_start_screen(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        Output.print_start_screen()
        sys.stdout = sys.__stdout__

        self.assertEqual("\n          \\             /\n           \\   o ^ o   /            \n            \\ (     ) /\n ____________(%%%%%%%)____________      \n(     /   /  )%%%%%%%(  \\   \\     )          \n(___/___/__/           \\__\\___\\___)\n   (     /  /(%%%%%%%)\\  \\     )\n    (__/___/ (%%%%%%%) \\___\\__)        \n            /(       )\\ \n          /   (%%%%%)   \\ \n               (%%%) \n                 !                      \n    Spelling Bee Game by PyGame\n      \n", captured_output.getvalue())

    def test_print_current_puzzle(self):
        class PuzzleStats:
            def __init__(self):
                self.rank = 1
                self.score = 0
                self.maxScore = 100
                self.guesses = ['word1', 'word2', 'word3']
                self.shuffled_puzzle = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
            
            def get_rank(self):
                return self.rank

        captured_output = io.StringIO()
        sys.stdout = captured_output
        stats = PuzzleStats()
        Output.print_current_puzzle(stats)
        sys.stdout = sys.__stdout__

        self.assertIn("Rank: 1", captured_output.getvalue())
        self.assertIn("Score: 0 / 100", captured_output.getvalue())
        self.assertIn("Words Guessed: word1 word2 word3", captured_output.getvalue())
        self.assertIn(">--<   d    >--<", captured_output.getvalue())
        self.assertIn("Commands: /Help /Shuffle /ShowAll /Back /Share /SaveGame /Exit", captured_output.getvalue())

    def test_with_longer_guesses_list(self):
        guesses = ['word1', 'word2', 'word3', 'word4', 'word5']
        result = Output.get_pretty_guesses(guesses)
        self.assertEqual(result, "word5 word4 word3 word2 ")
        

    def test_with_shorter_guesses_list(self):
        guesses = ['word1', 'word2']
        result = Output.get_pretty_guesses(guesses)
        self.assertEqual(result, "word1 word2 ")


    def test_print_main_menu(self):
        # Capture the output of the print statement
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Call the function
        Output.print_main_menu()

        # Reset the captured output
        sys.stdout = sys.__stdout__

        # Check if the printed string is as expected
        expected_output = '\n/NewGame\n/LoadGame\n/StartFromKey\n/Help\n/Exit\n\n'
        self.assertEqual(captured_output.getvalue(), expected_output)
    
    def test_print_exit(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        Output.print_exit()

        sys.stdout = sys.__stdout__

        expected_output = "\nConfirm exit?\ny\nn\n\n"
        self.assertEqual(captured_output.getvalue(), expected_output)


    def test_print_game_save(self):
        # Capture the output of the print function
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Call the function being tested
        Output.print_game_save()

        # Reset redirect
        sys.stdout = sys.__stdout__

        # Check the captured output
        expected_output = "\nSave Game?\ny\nn\n\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_print_load_game(self):
        # Capture the output of the print function
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Call the function being tested
        Output.print_load_game()

        # Reset redirect
        sys.stdout = sys.__stdout__

        # Check the captured output
        expected_output = "\nLoad Game?\ny\nn\n\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_print_load_options(self):
        # Capture the output of the print function
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Call the function being tested
        Output.print_load_options()

        # Reset redirect
        sys.stdout = sys.__stdout__

        # Check the captured output
        expected_output = "All Saved Games:\n-- " + "\n-- ".join(Output.get_load_options()).replace('.json','') + "\n\n(Type just the name in):\n\nSelect Game to load:\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_print_base_input(self):
        # Capture the output of the print function
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Call the function being tested
        Output.print_base_input()

        # Reset redirect
        sys.stdout = sys.__stdout__

        # Check the captured output
        self.assertEqual(captured_output.getvalue(), "Enter a panagram with seven unique letters: \n")


    def testprint_guess_outcome0(self):
        # Capture the output of the print function
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Call the function being tested
        result = Output.print_guess_outcome(0)

        # Reset redirect
        sys.stdout = sys.__stdout__

        # Check the captured output
        self.assertEqual(captured_output.getvalue(), "\n\tCorrect!\n")
        # Check the returned result
        self.assertTrue(result)

    def test_print_guess_outcome_69420(self):
        # Capture the output of the print function
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Call the function being tested
        result = Output.print_guess_outcome(69420)

        # Reset redirect
        sys.stdout = sys.__stdout__

        # Check the captured output
        self.maxDiff = None
        
        self.assertEqual(captured_output.getvalue(), "\n          \\             /\n           \\   o ^ o   /            \n            \\ (     ) /\n ____________(%%%%%%%)____________      \n(     /   /  )%%%%%%%(  \\   \\     )          \n(___/___/__/           \\__\\___\\___)\n   (     /  /(%%%%%%%)\\  \\     )\n    (__/___/ (%%%%%%%) \\___\\__)        \n            /(       )\\ \n          /   (%%%%%)   \\ \n               (%%%) \n                 !\n              Congrats!\n      You Completed the Puzzle                      \n      \n")
        
        # Check the returned result
        self.assertFalse(result)


    def test_print_help(self):
        # redirect stdout to capture printed output
        sys.stdout = io.StringIO()

        # call the function to be tested
        Output.print_help()

        # get the printed output and store it in a variable
        result = sys.stdout.getvalue()

        # reset stdout
        sys.stdout = sys.__stdout__

        # check if the result is as expected
        expected = "\n\nInstructions\n\nCreate words using letters from the hive and try to get the maximum score. \nWords must have at least four letters and include the center letter in brackets.\nAll optional letters will be surrounding the required center letter.   \nLetters can be used more than once. \nWords with hyphens, proper nouns, vulgarities, and especially obscure words are not in the word list. \nScore points to increase your rating. \n4-letter words are worth 1 point each.\nLonger words earn 1 point per letter. \nEach puzzle includes at least one “pangram” which uses every letter. \nThese are worth 7 extra points!\nFeedback/File Bug Report: <custom url>\n\nCommands\n/NewGame         /Loads a new game\n/LoadGame        /Loads a saved game\n/StartFromKey    /Enter a 7 letter key to start a new puzzle\n/Share           /copies the key to your clipboard\n/Help            /get instructions and commands \n/Exit            /exits the game\n\nEnter any key to continue...\n\n"
        self.assertEqual(result, expected)

    def test_print_help(self):
        # redirect stdout to capture printed output
        sys.stdout = io.StringIO()

        # call the function to be tested
        Output.print_game_over()

        # get the printed output and store it in a variable
        result = sys.stdout.getvalue()

        # reset stdout
        sys.stdout = sys.__stdout__

        # check if the result is as expected
        expected = "\n          \\             /\n           \\   o ^ o   /            \n            \\ (     ) /\n ____________(%%%%%%%)____________      \n(     /   /  )%%%%%%%(  \\   \\     )          \n(___/___/__/           \\__\\___\\___)\n   (     /  /(%%%%%%%)\\  \\     )\n    (__/___/ (%%%%%%%) \\___\\__)        \n            /(       )\\ \n          /   (%%%%%)   \\ \n               (%%%) \n                 !\n              Congrats!\n      You Completed the Puzzle                      \n      \n"
        self.assertIn(result, expected)

    def test_print_all_guesses(self):
        class MockStats:
            def __init__(self):
                self.guesses = ['guess1', 'guess2', 'guess3', 'guess4', 'guess5', 'guess6', 'guess7', 'guess8']
        stats = MockStats()

        captured_output = io.StringIO()
        sys.stdout = captured_output

        Output.print_all_guesses(stats)
        sys.stdout = sys.__stdout__

        expected_output = '\t SHOW ALL GUESSES\n\t\tguess1, guess2, guess3, guess4, \n\t\tguess5, guess6, guess7, guess8, \n\t\t\n\t Enter any key to continue...\n'
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_get_load_options(self):
        # First, create a "Saves" directory in the current working directory
        os.mkdir("SavesTest")

        # Next, create a few sample files in the "Saves" directory
        with open("Saves/save1.txt", "w") as f:
            f.write("Sample save data")
        with open("Saves/save2.txt", "w") as f:
            f.write("Sample save data")
        with open("Saves/save3.txt", "w") as f:
            f.write("Sample save data")

        # Call the `get_load_options` function to retrieve a list of the save files
        options = Output.get_load_options()

        # Assert that the `options` list contains the correct filenames
        self.assertIn("save1.txt", options)
        self.assertIn("save2.txt", options)
        self.assertIn("save3.txt", options)

        # Finally, clean up by removing the "Saves" directory and its contents
        os.rmdir("SavesTest")

        
    def test_get_detailed_response(self):
        # Test case when outcome is False
        captured_output = io.StringIO()
        sys.stdout = captured_output
        Output.get_detailed_response(False)
        self.assertEqual(captured_output.getvalue(),'\n\t... Guessed word was already used ...\n')
    
        # Test case when outcome is 1
        captured_output = io.StringIO()
        sys.stdout = captured_output
        Output.get_detailed_response(1)
        self.assertEqual(captured_output.getvalue(), '\n\t... Input is not in the Scrabble Dictionary ...\n')
        
    
        # Test case when outcome is 100
        captured_output = io.StringIO()
        sys.stdout = captured_output
        Output.get_detailed_response(100)
        self.assertEqual(captured_output.getvalue(), '\n\t... Input is shorter than four letters ...\n')
        
    
        # Test case when outcome is 200
        captured_output = io.StringIO()
        sys.stdout = captured_output
        Output.get_detailed_response(200)
        self.assertEqual(captured_output.getvalue(), '\n\t... Input does not contain the required letter ...\n')
    
    # Test case when outcome is 300
        captured_output = io.StringIO()
        sys.stdout = captured_output
        Output.get_detailed_response(300)
        self.assertEqual(captured_output.getvalue(), '\n\t... Input has non-given letters ...\n')
       
    
    # Reset the stdout
    sys.stdout = sys.__stdout__


if __name__ == '__main__':
    unittest.main()