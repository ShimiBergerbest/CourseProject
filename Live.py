
class Live():
    game_to_play, level_to_play = 0, 0
            
    def welcome(self, name):

        self.my_name = name
        return "Hello " + name + " and welcome to the World of Games (WoG).\n" + "Here you can find many cool games to play."

    def load_game(self):
        print("Please choose a game to play:")
        print("  1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
        print("  2. Guess Game - guess a number and see if you chose like the computer")
        print("  3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
        
        while True:
            self.game_to_play = input("\nGame to play (1-3):")
            try:
                x = int(self.game_to_play)
                if (x > 0 and x < 4):
                    print("Selected Game:", x)
                    break
                else:
                    print("Please select game between 1-3")

            except Exception:
                print("Selection must be number between 1 -3")

        print("\nPlease choose game difficulty from 1 to 5:")
        while True:
            self.level_to_play = input("level to play:")
            try:
                x = int(self.level_to_play)
                if (x > 0 and x < 6):
                    print("You choosed to play at level: ", x)
                    break
                else:
                    print("Please select level between 1-5")

            except Exception:
                print("Level must be number between 1 -5")

        # print("Grate! you select Game", self.game_to_play, "at Level:" , self.level_to_play)



