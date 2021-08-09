import Score as score 
from Utils import screen_cleaner 

class Game:
    
    difficulty = 0

    def print_welcom(self, game):
        print("*********************************")
        print("*** whelcome to the " + game + " ***")
        print("*** (to stop the game Ctrl+c) ***")
        print("*********************************")

    def print_results(self, win, difficulty):
        if win:
            print("\t\t\\|/ ____ \\|/")       
            print("\t\t @~/ ,. \\~@")        
            print("\t\t/_( \\__/ )_\\")       
            print("\t\t   \\__U_/")
            print ("\t*** Grate! you did it :-) ***")
            score.add_score(difficulty)
        else:
            print("\t\t    ____    ")       
            print("\t\t @~/ ,. \\~@")        
            print("\t\t  (   O  )")       
            print("\t\t   \\__-_/")
            print("\t*** Try next time :-( ***")

    def should_play_again(self):

        b = input("\nTo play once more? (y\\n):\n(note - when continue the screen wiil clean)\n")
        if b == 'y'.lower() or b == "yes".lower():
            screen_cleaner()
            return True
        else:
            return False