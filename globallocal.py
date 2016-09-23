variable = 'yes'
variable2 = 'yes'

def function(): #everything in a function is local
    global variable #modifying a global variable in a local scope
    variable2 = 'no' #modifies variable2 locally only
    variable = 'yes' #modifies variable globally

variable = 'waat' #modifies the global variable
print(variable) 
