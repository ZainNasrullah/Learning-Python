

import re, pyperclip

#Create a regex for phone numbers
phoneRegex = re.compile(r'''
#need to cover all use cases xxx-xxx-xxxx, xxx-xxxx, (xxx) xxx-xxxx, xxx-xxxx ext xxxx

(                                  #creates a tuople holding combination of this data
((\d\d\d) | (\(\d\d\d\)))?          #area code (optional)
(\s|-)                              #first separator
\d\d\d                              #first 3 digits
-                                  #second separator
\d\d\d\d                           #last four digits
(((ext(\.)?\s)|x)(\d{2,5}))?        #extension (optional)
)    

''', re.VERBOSE)

#Create a regex for e-mail address
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+  #name part
@                #at symbol
[a-zA-Z0-9_.+]+  #domain name part
''', re.VERBOSE)

#get the text from the clipboard
text = pyperclip.paste()

#extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

#take only the first entry in the truple (the combined phone #)
PhoneNumbers = []
for phoneNumber in extractedPhone:
    PhoneNumbers.append(phoneNumber[0])

print(extractedPhone)
print(PhoneNumbers)
