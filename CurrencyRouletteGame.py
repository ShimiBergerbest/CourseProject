import requests
import random as r
from Game import Game

class CurrencyRouletteGame(Game):

    currncy_rate = 0

    def get_money_interval(self):
        # https://free.currencyconverterapi.com/
        try:
            url = 'https://free.currconv.com/api/v7/convert?apiKey=9fd107fb0c0bce359238&q=USD_ILS&compact=y'
            response = requests.get(url)
            data = response.json()
            self.currncy_rate = float(data["USD_ILS"]["val"])
            
        except:
            print("Can't Get\Parss\Convert currncy... check if you are online and site is up")

    def get_guess_from_user(self):
        amount = r.randint(1, 100)
        total_amount = amount * self.currncy_rate
        user_guess = 0.0

        print("(*** lecturer's hint : ", str(total_amount), "***)") 

        while True:
            input_str = "Please guess of value to a given amount of " + str(amount) + " in USD: "
            x = input(input_str)
            try:
                user_guess = float(x)
                print("user_guess enterd: ", user_guess)
                break
            except:
                print("Must be number between (e.g. 3 or 87.45)  ")
                continue

        
        if user_guess > (total_amount - self.difficulty) and user_guess < (total_amount + self.difficulty):
            # print("Grate", self.currncy_rate, " ", (self.currncy_rate - self.difficulty))
            return True
        else:
            return False
            # print("Next time")                      

    
    def play(self, difficulty):

        self.difficulty = difficulty
        self.print_welcom("Currency Roulette Game")

        while True:
            try:
                if self.get_money_interval() == 0:
                    print("A fatal error occur, see you next time")
                    break

                self.print_results(self.get_guess_from_user(), difficulty)
                answer = self.should_play_again()
                if  answer == 0:
                    print("See you next time")
                    return 0
                elif answer == 2:
                    print("\nLet's play new again....\n")
                    return 2
                elif answer == 1:
                    print("\nLet's play again....\n")

            except KeyboardInterrupt:
                print("\nSee you next time\n")
                break
        
        

### test    
def main():

    x = CurrencyRouletteGame()
    x.play(5)

if __name__ == "__main__":
    main()
    