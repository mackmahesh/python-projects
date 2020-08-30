import random
import time

print("\nWelcome to Hangman game by Mahesh\n")
name = input("Enter your name\n")
print("Hello!!\t"+ name + "\t Lets begin!!")
time.sleep(2)
print("   The game is about to start!!\n")
time.sleep(3)

def main():
    global word_list
    global word
    global length
    global display
    global already_gussed
    global count
    global word_is
    global count
    global take
    word_list = ['dinner','fun','great','apple','guess','moango','bananna']
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
        take =input('\n In valid option, Please type again y for Yes or else n for No.:')
    if take == 'y'or 'Y' :
        print("\nLets play again")
        main()
    elif take == 'n' or 'N' :
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
    global word_is
    limit = 5
    guess = input("Welcome to Hangman  :" + display + "  Enter your wild guess:\n")
    guess = guess.strip()


    if len(guess.strip()) == 0 or len(guess.strip()) > 1:
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
            print("Wrong guess: "+str(limit-count)+"  You have few days to live")


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
            print("Wrong guess: "+str(limit-count)+"  You have few days to live")

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
            print("Wrong guess: "+str(limit-count)+" You have few days to live")

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
            print("Wrong guess: "+str(limit-count)+" You have few days to live")

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
            print("Wrong guess. Thanks for playing")
            print("The word was:",word_is)
            loop()
    if word == "_" * length:
        print("Congrats You did it!")
        loop()
    elif count!= limit  :

        hangman()

main()

hangman()
