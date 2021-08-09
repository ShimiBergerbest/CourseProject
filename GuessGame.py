import random as r
from Game import Game

class GuessGame(Game):

    secret_number = 0, 0

    def generate_number(self, difficulty):
        self.secret_number = r.randint(1, difficulty)
        self.difficulty = difficulty
        print("(*** lecturer's hint : ", str(self.secret_number), "***)") 

    def get_guess_from_user(self):
        s = "Enter number between 1 and " + str(self.difficulty) + " : "
        print()
        x = input(s)
        print()
        print("You enterd ", x)
        return int(x)

    def compare_results(self, n):
        if n == self.secret_number:
            return True
        else:
            return False

    def play(self, difficulty):
        self.print_welcom("Currency Guess Game")
        d = difficulty
        print("\nLet's play....")
        while True:
            try:
                self.generate_number(d)
                x = self.get_guess_from_user()
                self.print_results(self.compare_results(x), difficulty)
                if not self.should_play_again():
                    print("See you next time")
                    break
                print("\nLet's play again....")
            except KeyboardInterrupt:
                print("See you next time")
                break

### test    
def main():
    x = GuessGame()
    x.play(5)

if __name__ == "__main__":
    main()
