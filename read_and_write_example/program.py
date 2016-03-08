

#reads a text file
# with open will run all code below and then close the file after you are done

with open("words.txt","r+") as  word_list:
    for i, line in enumerate(word_list): # enumerate adds a 0-range number to each line
        print(line)
        print(i)

def pick_random_word():
