def guessinggame():
    from random import randint  
    number = randint(1, 11)
    name = raw_input("What is your name? ")
    print "Hi %s"  % name
    print "%s I'm thinking of a number between 1 and 11. Try to guess my number" % name 

    guesses = 0
    while True:
        guesses += 1

        try:
            guessed_number = int(raw_input("What is your guess? "))
            if guessed_number == number:
                print "YAY! Congratulations"
                play_again = raw_input("Would you like to play again? ")
                if play_again == 'yes':
                    print guessed_number
                else:
                    break

            elif guessed_number > number:
                print "That is too high. Please try again!"

            elif guessed_number < number:
                print "That is too low. Please try again!"

            elif guessed_number > 11:
                print "Outta range"

        except ValueError:
                print "That's not a number!"



 
guessinggame()