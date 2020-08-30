import random
import time

print("\nWelcome to Hangman game by Mahesh\n")
name = input("Enter your name\n")
print("\t Hello!!" + name + "\t Lets begin!!")
time.sleep(2)
print("The game is about to start!!\n")
time.sleep(3)

def main():
    global word_list
    global word
    global length
    global display
    global already_gussed
    global count
    word_list = ['mahesh','fun','great','stunt','guess']
    word = random.choice(word_list)
    word_is = word
    length = len(word)
    display = '_' * length
    already_gussed = []
    count = 0
    take = ""

def loop():
    global take
    take = input("Do you want to play again.....Type y for yes or n for no: ")
    while take not in ['y','n','Y','N']:
        print('\n In valid option, Please type again y for Yes or else n for No.:')
    if take == 'y'or 'Y' :
        print("\nLets play again")
        main()
    else:
        print("\n Thanks for playing, will catch you later")
        exit()
def hangman():
    global count
    global guess
    global index
    global word
    global display
    global already_gussed
    global take
    limit = 5
    guess = input("Welcome to Hangman\t" + display + "\t Enter your wild guess:\n")
    guess = guess.strip()


    if len(guess) == 0 or len(guess) > 1:
        print("\n It is an invalid guess")
        print("Dumbo it is hangman!! You should check one word at a time!")
        hangman()
    elif guess in word:
        already_gussed.extend([guess])
        index = word.find(guess)
        word = word[:index] + '_' + word[index+1:]
        display = display[:index] + guess + display[index+1:]
        print("\n")
        print(display)


    elif guess in already_gussed:
        print("Try again!")

    else:
        count+=1
        if count == 1:
            print("U are about to see your future!!\n")
            print("   _____ \n"
                  "  |     | \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__\n")
            print("Wrong guess\t"+str(limit-count)+"\t You have few days to live")


        elif count == 2:
            print("U are about to see your future!!\n")
            print("   _____ \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__\n")
            print("Wrong guess\t"+str(limit-count)+"\tYou have few days to live")

        elif count == 3:
            print("U are about to see your future!!\n")
            print("   _____ \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__\n")
            print("Wrong guess\t"+str(limit-count)+"\t You have few days to live")

        elif count == 4:
            print("U are about to see your future!!\n")
            print("   _____ \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    / \ \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__\n")
            print("Wrong guess \t"+str(limit-count)+"\t You have few days to live")

        elif count == 5:
            print("U are about to see your future!!\n")
            print("   _____ \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    / \ \n"
                  "  |     |  \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess \t"+str(limit-count)+"\t You have few days to live")
            print("The word was:",word_is)
            loop()
    if word == "_" * length:
        print("Congrats You did it!")
        loop()
    elif limit != count :
        hangman()

main()

hangman()
