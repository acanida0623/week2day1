import random
import linecache
import graphics
import time
import urllib.request





def get_letter(letters):
    alpha = "abcdefghijklmnopqrstuvwxyz"

    while True:
        letter_guess = str(input("Please guess a letter. ")).lower()
        #make sure input is a single letter not already guessed
        if letter_guess not in alpha:
            print("That is not a single letter. ")
            continue


        if letter_guess in letters:
            print("You've already guessed that letter. ")
            continue
        return str(letter_guess).lower()




def main():
    print('H A N G M A N')
    missed_letters = ''
    correct_letters = ''
    secret_word = get_random_word()
    game_is_done = False
    # while True: Display the board
    while True:
        graphics.display_board(missed_letters,correct_letters,secret_word)
        # Let the player type in a letter
        letter_guess = get_letter(missed_letters+correct_letters)

        #Check if guess letter is correct
        if letter_guess in secret_word:
            correct_letters += letter_guess

            # Check if the player has won
            found_word = True

            for x in range(len(secret_word)):
                if secret_word[x] not in correct_letters:
                    found_word = False
                    break

            if found_word:
                    print("Congratulations! The secret word was {word}! ".format(word=secret_word))
                    game_is_done = True

                    time.sleep(5)


        else:
            missed_letters += letter_guess
            print()
            print("Nope! There is no {0}'s' in the word.".format(letter_guess))
            print()

        # Check if player has guessed too many times and lost
        if len(missed_letters) == len(graphics.HANGMANPICS) - 1:

            graphics.display_board(missed_letters,correct_letters,secret_word)

            print()
            print("You lose! The word was {0}. ".format(secret_word))


            time.sleep(5)

            game_is_done = True


        # Ask the player if they want to play again (but only if the game is done).
        if game_is_done:
            play_again = str(input("Do you want to play again? (Y)es ")).lower()
            if play_again == 'y' or play_again == 'yes':
                missed_letters = ''
                correct_letters = ''
                secret_word = get_random_word()
                game_is_done = False
            else:
                break




def count_lines():
    #count the number of lines/words in the text file
    with open('words.txt') as f:
        for i, l in enumerate(f):
            pass

    return i + 1




def get_random_word():
    #get a random line, linecache adds a space at the end of the string so delete it with slicing before return
    with urllib.request.urlopen("http://randomword.setgetgo.com/get.php") as response:
        word = response.read()
        print(word.decode('utf8'))
        return (word.decode('utf8'))
    #word = linecache.getline("words.txt",random.randint(0,count_lines()))
    #word = word[:-1]
    #print(word)
    #return word

main()
