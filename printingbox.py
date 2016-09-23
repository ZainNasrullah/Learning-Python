

def PrintBox(symbol, width, height):

    if len(symbol) != 1:
        raise Exception("Your symbol needs to be a string of length 1")
    if (width < 2) or (height < 2):
        raise Exception("Your height or width are too small!")
    
    print(symbol * width)
    
    for row in range(height-2):
        print(symbol + (" " * (width-2)) + symbol)
    print(symbol * width)

PrintBox('*',10,5)
PrintBox('z', 2,1)
