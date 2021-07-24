'''This program contains the functions averageFinder and midpointFinder. AverageData calculates the averages of the
"columns" of a list of numbers (a list of lists of numbers) for real and fake samples (separately) and midpointFinder
finds the midpoint between the real and fake averages.
Data is either given from the test case or from user input, which is run through incomingData.
Assignment 2: classifier_builder
Name: Anna Wood
Student Number: 20091785
NetID: 17aaw2'''

def averageFinder(sample_data):
    '''will take a list of attributes and:
    averageFinder calculates the average of each of the attributes across all the samples with the
    same classification (0 or 1)
    input: sample list / list of numbers
    output: none, averages are passed to midpointFinder
    note - 1 IS REAL 0 IS COUNTERFEIT
        '''

    real_avgs_counter = 0
    counter_avgs_counter = 0
    real_avgs = []
    counter_avgs = []
    avg_len_real = 0
    indx = 0

    while indx < 4: # while-loop that sums each attribute and adds it to the list of its category (real or counter)
        for i in range(0,len(sample_data)): # loop to separate data into 0 and 1
            if sample_data[i][4] == 1:
                real_avgs_counter += sample_data[i][indx]# if real, attribute is summed in counter
                avg_len_real = avg_len_real + 1 /4 # used to count the length of how many real bills
            elif sample_data[i][4] == 0: # attribute sum for counterfeit bills
                counter_avgs_counter += sample_data[i][indx]


        real_avgs.append(real_avgs_counter) # after each attribute is summed it is added to the final list
        counter_avgs.append(counter_avgs_counter)

        real_avgs_counter = 0 # counters are reset to 0 after each list
        counter_avgs_counter = 0

        indx += 1 # index for counting the "columns"

    avg_len_counter = len(sample_data) - avg_len_real # number of real / counter bills calculated for finding the average

    for i in range(0, 4): # divides the real, counterfeit sums by the amount of real & counterfeit items respectively
        real_avgs[i] = round((real_avgs[i] / avg_len_real), 3)
        counter_avgs[i] = round((counter_avgs[i] / avg_len_counter), 3) # each average rounded to 3 decimal points

    return real_avgs, counter_avgs



def midpointFinder(real_avgs, counter_avgs):
    '''part 2 of the building classifier, takes the averages of the real and and fake samples and finds
    the midpoint  (divides by 2). midpoints list should then be returned to classifier
    for further classifying
    input: averages of real, fake samples
    output: midpoints (returned to incomingData)'''


    midpoints = [] # empty list for midpoints

    for i in range(0,4): # finds midpoints by adding averages and dividing by 2
        midpoint = (real_avgs[i] + counter_avgs[i]) / 2
        midpoints.append(round(midpoint,3))

    return midpoints #returns midpoints to incomingData



def incomingData(training_data):
    '''function runs from here when data is passed from our main interface
    input: training_data
    output: midpoints'''

    real_avgs, counter_avgs = averageFinder(training_data)
    midpoints = midpointFinder(real_avgs, counter_avgs)
    return midpoints # midpoints returned to main interface



if __name__ == '__main__':
    sample_data_main = [[ 3, 8, -2, 0, 0], [4, 8, -2, -1,0],[3, -2, 1, 0, 0], [2, 1, 0, -2, 0], # fake samples (5th item 0)
                    [0, 3, -3, -2, 1], [-3, 3, 0, -3, 1],
                    [-6, 7, 0, -3, 1] ] # real samples (5th item is 1)
    real_avgs , counter_avgs = averageFinder(sample_data_main)
    midpoints = midpointFinder(real_avgs, counter_avgs)

    print('real averages (test case)',real_avgs, 'should be -3 , 4.333, -1. -2.667')
    print('counter averages (test case)',counter_avgs, 'should be 3, 3.75, -0.75, -0.75')
    print('midpoints (test case)', midpoints, 'should be 0, 4.041 ish, -0.875, -1.708')
