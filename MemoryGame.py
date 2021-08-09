import random as r
import time
import ctypes
import threading
import sys

# if "win" in sys.platform:
#     from tkinter.commondialog import Dialog

from Game import Game

class MemoryGame(Game):
    random_numbers = []
    user_list = []
    number_str = ["first","second","third","fourth","fifth"]

    def worker(self, title, close_until_seconds):
        time.sleep(close_until_seconds)
        wd=ctypes.windll.user32.FindWindowW(0,title) ######
        ctypes.windll.user32.SendMessageW(wd,0x0010,0,0) ######
        return

    # def AutoCloseMessageBoxW(self, text, title, close_until_seconds):

    #     t = threading.Thread(target=self.worker,args=(title, close_until_seconds))
    #     t.start()
    #     ctypes.windll.user32.MessageBoxW(0, text, title, 0) ######


    def generate_sequence(self):
        selecter_numbers = ""
        while True:
            t = r.randint(1, 101)
            if t in self.random_numbers:
                continue
            else:
                self.random_numbers.append(t)
                selecter_numbers += str(t)
                selecter_numbers += "  "

            if len(self.random_numbers) == self.difficulty:
                break  

        print("(*** lecturer's hint : ", self.random_numbers, "***)") 

        # try:
            # is_win = False
            # if "win" in sys.platform:
            # # if is_win:
            #     self.AutoCloseMessageBoxW(selecter_numbers,"Try to remember" , 0.7)
            # else:
        sys.stdout.write(selecter_numbers)
        sys.stdout.flush()
        time.sleep(0.7)
        for i in selecter_numbers:
            sys.stdout.write('\b')

        # except:
        #     print("This game fit to windows popup at the moment, other os will see it on consol")

    def get_list_from_user(self):
        x = 0
        while len(self.user_list) != len(self.random_numbers):
            i = input("Please enter "+ self.number_str[x]  + " number: ")
            try:
                y = int(i)
                self.user_list.append(y)
                x +=1
            except:
                print("Must be a number only") 

    def is_list_equal(self):

        print("User List: " , self.user_list, " randome numbers : ", self.random_numbers)
        for i in self.random_numbers:
            if i not in self.user_list:
                return False
        return True

    def play(self, difficulty):
        self.print_welcom("Memory Game")
        self.difficulty = difficulty
        print("\nLet's play....")
        while True:
            try:
                self.generate_sequence()
                self.get_list_from_user()
                self.print_results(self.is_list_equal(), difficulty)
                self.random_numbers = []
                self.user_list = []
                if not self.should_play_again():
                    print("See you next time")
                    break
                print("\nLet's play again....")
            except KeyboardInterrupt:
                print("See you next time")
                break
### test    
def main():
    x = MemoryGame()
    x.play(5)

if __name__ == "__main__":
    main()
