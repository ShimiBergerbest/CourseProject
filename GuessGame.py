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
        t_x = 0
        while True:
            try:
                x = input(s)
                print("You enterd ", x)
                print()
                t_x = int(x)
                break
            except:
                print("Input must be a number")

        return int(t_x)

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
                answer = self.should_play_again()
                if answer == 0:
                    print("See you next time")
                    return 0
                elif answer == 2:
                    print("\nLet's play new again....\n")
                    return 2
                elif answer == 1:
                    print("\nLet's play again....\n")

            except KeyboardInterrupt:
                print("See you next time")
                break

### test    
def main():
    x = GuessGame()
    x.play(5)

if __name__ == "__main__":
    main()
