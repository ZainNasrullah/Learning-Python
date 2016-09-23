def div(number,divideby):
    try:
        return (number/divideby)
    except ZeroDivisionError: #can have a basic except with no type
        print("You tried to divide by zero")

def Cats():
    numCats = 0
    while numCats == 0:
        
        print("How many cats do you have?")
        numCats = input()
        
        try:
            if (int(numCats) > 5):
                print("That's a lot of cats")
            elif (int(numCats) < 0):
                print("How do you have negative cats? That doesn't even make any sense")
                numCats = 0
            else:
                print("That's not a lot of cats")
        except ValueError:
            print("You did not enter a number.")
            numCats = 0
    
Cats()
