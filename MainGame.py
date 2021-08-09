from GuessGame import GuessGame 
from MemoryGame import MemoryGame
from CurrencyRouletteGame import CurrencyRouletteGame
from Live import Live
   
def main():
    
    live = Live()
    my_name = input("Please type you name: \n")
    print (live.welcome(my_name))
    live.load_game()

    print ("Selected game:", live.game_to_play, " on level ", live.level_to_play)

    if (int(live.game_to_play) == 1):
        memory_game = MemoryGame()
        memory_game.play(int(live.level_to_play))

    elif (int(live.game_to_play) == 2):
        guess_game = GuessGame()
        guess_game.play(int(live.level_to_play))

    elif (int(live.game_to_play) == 3):
        currency_roulette_game = CurrencyRouletteGame()
        currency_roulette_game.play(int(live.level_to_play))
    else:
        print("Something got wrong... call 911")
        raise ValueError("no game can be found for ", live.game_to_play)


if __name__ == "__main__":
    main()