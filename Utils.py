import os
from time import sleep

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = ["Score file not exists", "Illegal score values" ]

def screen_cleaner():
   # for mac and linux(here, os.name is 'posix')
    print("Before continuing, about to clean the console in 2 second  ...")
    sleep(2)
    if os.name == 'posix':
        _ = os.system('clear')
    else:
    # for windows platfrom
        _ = os.system('cls')


