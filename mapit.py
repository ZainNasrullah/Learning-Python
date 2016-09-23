import webbrowser, sys, pyperclip

sys.argv # ['mapit.py, '870', 'Valencia', 'St.']

#check if command line arguments were passed
if len(sys.argv)>1:
    # convert the address into a single string separated by a space
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# https://www.google.com/maps/place/<address>
webbrowser.open('https://www.google.com/maps/place/'+address)
