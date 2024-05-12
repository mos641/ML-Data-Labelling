import setup, calculations

# Author: Mostapha A
# Program to predict an items classification based on predefined data

# ask for item classification name
classname = input("Enter name of the item classification (e.g vehicle type, player position)\n > ")

# Call setup functions to define data set being used

# how many attributes each label/class uses
numofat = setup.enter_attribute_count(classname)

# ask for attribute names
allnames = setup.enter_names(numofat)

#ask for how many classes there are
numofclass = setup.enter_class_count()

# ask for each class name
classes = setup.enter_class_names(classname, numofclass)

# populate dataset that calculations will be based on
i = 0
j = 1
allatts = []
attributes = []
# loop through each class
while i < numofclass:
    singleatts = []
    print(f"\nEnter {classes[i]} {j} attributes")
    # loop through and get each attribute
    for att in allnames:
        num = setup.enter_attribute(classes[i], att)
        
        #store the attribute
        singleatts.append(num)
    
    # append to all attributes
    allatts.append(singleatts)
    
    # ask if they want to add another of the same class
    userinput = 't'
    while userinput not in ("y","Y","n","N"):
        userinput = input(f"Add another {classes[i]}? \"y\" for yes or \"n\" for no\n > ")
        
    # if they do, pass otherwise increment i to go to the next class
    if userinput in ("y","Y"):
        pass
        j += 1
    else:
        attributes.append(allatts)
        allatts = []
        i += 1
        j = 1
     

# call functions to perform calculations
averages = calculations.calculate_averages(attributes, numofat)
weights = calculations.calculate_weight(averages, numofclass, numofat)


# loop through menu of program
menuoption = 't'
# loop until they quit
while menuoption not in '3':
    menuoption = 't'
    # validate their input
    while menuoption not in ("1", "2", "3"):
        menuoption = input("1. Guess a classification\n2. Enter new data\n3. Quit program\n > ")
    
    # implement menu options
    if  menuoption == '1':
        # guess based on data, take in attributes
        singleatts = []
        print(f"\nEnter {classname}'s attributes")
        # loop through and get each attribute
        for att in allnames:
            num = setup.enter_attribute(classname, att)
            
            #store the attribute
            singleatts.append(num)
        
        # get the scores
        scores = calculations.score_data(weights, averages, singleatts)
        
        # print the most likely one
        print(f"This is a {classes[scores.index(max(scores))]}\n")
        
        # print the verdict
    elif menuoption == '2':
        # add more data, ask which class first
        userinput = 't'
        # ensure it is one of the defined classes
        while userinput not in classes:
            userinput = input(f"Which {classname} would you like to add to?\n > ")
            if userinput not in classes:
                print(f"Enter one of your predefined classes {classes}. Try again.")
        
        # add more data for the selected class
        index = classes.index(userinput)
        singleatts = []
        print(f"\nEnter new {classes[index]} attributes")
        # loop through and get each attribute
        for att in allnames:
            num = setup.enter_attribute(classes[index], att)
        
            #store the attribute
            singleatts.append(num)
            
        #store new attributes with the rest of the data
        attributes[index].append(singleatts)
        
        # perform calculations again
        averages = calculations.calculate_averages(attributes, numofat)
        weights = calculations.calculate_weight(averages, numofclass, numofat)
        
    elif menuoption == '3':
        print ("Good Bye.\n")
