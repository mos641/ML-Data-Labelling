# Author: Mostapha A
# Functions that perform all machine learning data calculations

# calculates the average for each attribute in each class
def calculate_averages(attributes, numofattributes):
    # loop thorugh attributes and calculate averages
    allaverages = []
    # loop through each classification
    for atts in attributes:
        i = 0
        averages = []
        # loop through each attribute
        while i < numofattributes:
            j = 0
            avg = 0
            # loop through each data set
            for instance in atts:
                # add all the data
                avg += instance[i]
                # j counts how many sets there are
                j += 1
            
            # increment i to move to the next attribute
            i += 1
            # add the average to our list
            averages.append(avg/j)
            
        #after each classification append the averages to our list to return
        allaverages.append(averages)
    
    #return the list of all averages
    return allaverages


# calculates how each attribute should be weighed 
def calculate_weight(averages, numofclasses, numofattributes):
    alldiffs = []
    # loop through class
    for classification1 in averages:
        diffs = []
        attindex = 0 # attribute index
        total = 0
        # loop through each attribute
        for attribute in classification1:
            
            diff1 = -1
            diff2 = -1
            
            classindex = 0 # index for classes
            
            # loop through each class
            while classindex < numofclasses:
                # set a value as the attribute of the outer loops class
                value = classification1[attindex]
                
                # check that we are not comparing with itself
                if averages.index(classification1) == classindex:
                    pass
                else:
                    # subtract original attribute from the other classes same attribute
                    diff2 = value - averages[classindex][attindex]
                    if diff2 < 0:
                        # if it is negative make it positive
                        diff2 = diff2 * -1
                        
                    # if this is the first run through, set diff1 to diff2
                    if diff1 == -1:
                        diff1 = diff2
                    else:
                        # otherwise check if it is smaller and store if so
                        if diff2 < diff1:
                            diff1 = diff2
                classindex += 1
                #end inner loop
            attindex += 1
            total += diff1
            diffs.append(diff1)
            #end middle loop
        diffs.append(total)
        alldiffs.append(diffs)
        #end outer loop

    # take the differences and calculate the weights or percentages
    allweights = []
    j = 0
    # loop through each classes averages
    for instance in averages:
        weights = []
        i = 0
        # loop through each attribute and calculate the percentage/weight
        while i < numofattributes:
            if alldiffs[j][numofattributes] == 0:
                weights.append(0)
                i += 1
            else:
                weights.append(alldiffs[j][i]/alldiffs[j][numofattributes])
                i += 1
        
        # store and increment
        allweights.append(weights)
        j+=1
    
    return allweights


# takes in attributes values and scores it based on our predefined info
def score_data(weights, averages, data):
    scores = []
    i = 0 # index for which class
    # loop through each class in averages
    for instance in averages:
        j = 0 # index for each attribute
        score = 0
        # loop through each attribute
        for attribute in instance:
            # get a percentage of how close the input is to the class average
            if attribute > data[j]:
                mark = (data[j] / attribute) * 100
            else:
                mark = (attribute / data[j]) * 100
            
            # multiply this by the weight each attribute has
            score += (mark * weights[i][j])
            j += 1
        
        # increment and store the score
        i += 1
        scores.append(score)
    
    return scores
    
