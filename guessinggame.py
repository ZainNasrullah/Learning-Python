#Guess the number game
import random
count = 0

def Check(guess):
    global answer
    global a
    global b
    global count
    count+=1
    
    try: #evaluates the result of the guess
        guess = (int(guess))
        if (guess < int(a) or guess > int(b)):
            print("That's not in the range")
        elif (guess == answer):
            print("You got it!")
            return True #returns true if guess is the correct answer
        elif (guess > answer):
            print("Your guess is too high")
        else:
            print("Your guess is too low")
    except ValueError:
            print ("Your guess isn't a number silly!")
    return False #returns false if guess is not the correct answer

print("Please enter your name: ")
name = input()

check = False
while check == False:
    try:
        check = True
        print("Please enter the lower limit for the number guessing game: ")
        a = input()
        print("Please enter the upper limit for the number guessing game: ")
        b = input()
        answer = random.randint(int(a),int(b))
    except ValueError:
        print("You input is invalid, let's try again")
        check = False
    
    
    
check = False
while check == False:
    print("Guess a number: ")
    guess = input()
    check = Check(guess)

print("It took you " + str(count) + " guesses " + name)
            

