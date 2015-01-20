print "Welcome to the Guessing Game!"
name = raw_input("What is your name?")
print name
import random
number = random.randrange(1, 11)
print "%s, I'm thinking of a number between 1 and 100. Try to guess my number." % name

guesses = 0
while True:
    guesses += 1
  

    try:
        user_guess = int(raw_input("Guess a number:"))
    

        if user_guess < number:
            print "Your guess is not the number"
            if user_guess > 0:
                print "too low. try again"
            else:
                print "outta range"
       
        elif user_guess > number:
            print "Your guess is not the number"
            if  user_guess <=10:
                print "too high. try again"
            else:
                print "outta range"
        elif user_guess == number:
            print "Congrats, it took you %d tries" % guesses
            break  

    except ValueError:
        print "That's not a number!"
