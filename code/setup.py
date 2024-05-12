# Author: Mostapha A
# Functions for dealing with initial setup and entering labeled data

# Asks for and returns how many attributes each item will use
def enter_attribute_count(classname):
	numofat = -1
	# ask how many attributes there are loop for validation
	while (numofat == -1):
		userinput = input(f"How many numerical attributes will each {classname} have?\n > ")
		# try to convert to integer
		try:
			numofat = int(userinput)
			# if it is a valid number, break otherwise print error
			if numofat > 0:
				break
			else:
				print("Must be greater than 0. Try again.")
				numofat = -1
		except ValueError:
			# if it was not a number print so
			print ("Must be a whole number. Try again.")
			numofat = -1

	# return the validated input
	return numofat


# Asks for the names of each attribute and returns a list
def enter_names(num):
    i = 1
    names = []
    
    # loop for each attribute name
    while i <= num:
        userinput = input(f"Enter attribute {i} name: ")
        names.append(userinput)
        i += 1
    
    #return the list of names
    return names


# Asks for and returns how many different labels or classifiations to use
def enter_class_count():
    num = -1
    # enter how many classifications
    while (num == -1):
        userinput = input("How many classifications will there be?\n > ")
        # try to convert to integer
        try:
            num = int(userinput)
            # if it is a valid number, break otherwise print error
            if num > 0:
                break
            else:
                print("Must be greater than 0. Try again.")
                num = -1
        except ValueError:
            # if it was not a number print so
            print ("Must be a whole number. Try again.")
            num = -1
    #return validated input
    return num


# Asks for and returns a list of the names of each label or class
def enter_class_names(classname, num):
    i = 1
    names = []
    # loop for each class name
    while i <= num:
        userinput = input(f"Enter {classname} {i} type: ")
        names.append(userinput)
        i += 1
    
    #return the list of names
    return names


# Asks for and returns a validated attribute value
def enter_attribute(classification, attribute):
    num = -1
    #ask for the attribute value and validate it is an integer
    while num == -1:
        userinput = input(f"Enter {classification} {attribute}\n > ")
        # try to convert to int
        try:
            num = int(userinput)
            # check range
            if (num < 0):
                print("Attribute must be a positive value. Try again.")
                num = -1
                
        except ValueError:
            # if it wasnt an integer
            print("Attribute must be a whole numerical value. Try again.")
            num = -1
        
        #return the attribute
        return num