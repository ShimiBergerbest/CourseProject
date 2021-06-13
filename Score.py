from os import path
import Utils as u  

POINTS_OF_WINNING = 0

def get_score():
    last_score_t = "0"

    try:
        with open(u.SCORES_FILE_NAME, 'r+') as f:
            last_score_t = f.read()
            last_score = "<h1>The score is <div id=\"score\">" + str(int(last_score_t)) + "</div> </h1>" 
    except ValueError:
        last_score = "<h1><div id=\"score\" style=\"color:red\">" + u.BAD_RETURN_CODE[1] + "</div></h1>"
        print("no value in file")
    except FileNotFoundError:
        last_score = last_score = "<h1><div id=\"score\" style=\"color:red\">" + u.BAD_RETURN_CODE[0] + "</div></h1>"
        

    return last_score


def add_score(difficulty):

    if not path.exists(u.SCORES_FILE_NAME):
        sf = open(u.SCORES_FILE_NAME, 'w')
        sf.write("0")
        sf.close()

    last_score = 0
    with open(u.SCORES_FILE_NAME, 'r+') as f:
        last_score_t = f.read()
        try:
            last_score = int(last_score_t)
        except:
            last_score = 0
            print("no or illigal value in file, score will start from 0")

        point_of_winning = (difficulty * 3) + 5
        POINTS_OF_WINNING = point_of_winning + int(last_score)

    with open(u.SCORES_FILE_NAME, 'w') as f:
        f.write(str(POINTS_OF_WINNING))


### test    
def main():
    get_score()
    add_score(4)

if __name__ == "__main__":
    main()
