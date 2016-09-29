import pprint

message = "It was a bright cold day in April, and the clocks were striking thirteen"

# this is a blank dictionary
count = {}

# this script will run through the entire message and count each character
# in it
for character in message.upper():

    # if key doesn't exist, add it to dictionary and set default to 0
    count.setdefault(character, 0)
    # increment the value associated with the key by one
    count[character] += 1

# pretty print function (formats the dictionary cleanly and sorts):
# pprint.pprint(count)

# saves the dictionary as a string to the variable text
text = pprint.pformat(count)
print(text)
