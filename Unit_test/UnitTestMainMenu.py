import unittest
import io
import sys
from unittest.mock import patch
from mainmenu import *

class TestMainMenuHandler(unittest.TestCase):
    
    def test_new_game(self):
        with patch('builtins.input', side_effect=['/newgame', '', '/exit', 'y']):
            with patch('sys.exit') as exit_mock:
                main_menu_handler()
                self.assertTrue(exit_mock.called)
                
    def test_load_game(self):
        with patch('builtins.input', side_effect=['/loadgame', 'test_save', 'y']):
            with patch('sys.exit') as exit_mock:
                load_save_game()
                self.assertTrue(exit_mock.called)
                
    def test_key_start(self):
        with patch('builtins.input', side_effect=['puzzle', '/exit', 'y']):
            with patch('sys.exit') as exit_mock:
                keyStart()
                self.assertTrue(exit_mock.called)
                
    def test_active_game_loop(self):
        with patch('builtins.input', side_effect=['/exit', 'y']):
            with patch('sys.exit') as exit_mock:
                activeGameLoop()
                self.assertTrue(exit_mock.called)
                
    def test_start_new_game(self):
        with patch('builtins.input', side_effect=['/exit', 'y']):
            with patch('sys.exit') as exit_mock:
                start_new_game()
                self.assertTrue(exit_mock.called)
                
    def test_start_game_with_key(self):
        with patch('builtins.input', side_effect=['/exit', 'y']):
            with patch('sys.exit') as exit_mock:
                start_game_with_key('puzzle')
                self.assertTrue(exit_mock.called)
                
    def test_start_game_with_key_from_load(self):
        with patch('builtins.input', side_effect=['/exit', 'y']):
            with patch('sys.exit') as exit_mock:
                start_game_with_key_from_load((5, 'puzzle'))
                self.assertTrue(exit_mock.called)
                
    def test_save_current_game(self):
        with patch('builtins.input', side_effect=['save']):
            save_current_game('save')
            with open('save.txt') as f:
                self.assertEqual(f.read(), 'score=0\npuzzle="puzzle"\n\n')

if __name__ == '__main__':
    unittest.main()