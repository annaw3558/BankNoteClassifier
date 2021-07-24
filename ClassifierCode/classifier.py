'''Assignment 2: classifier
Name: Anna Wood
Student Number: 20091785
NetID: 17aaw2'''

def classifier(midpoints, testing_data):
    '''this classifier takes the midpoint values and runs through samples from the file testing.txt to
    see if each sample is real or fake. The determined authenticity is then compared to the samples actual
    authenticity (the 5th attribute). The accuracy of whether all the samples are correctly identified is
    calculated and returned to the main interface. The classification of each attribute compared to the
    midpoints can be found on our assignment page.
    input: midpoints (from training.txt through the classifier builder)
    output: accuracy of the classifier (percentage)
    note - 0 is counterfeit, 1 is real'''


    real_attr = 0 # used to count real attributes based off of midpoint classification
    fake_attr = 0 # used to count fake attributes based off of midpoint classification
    sample = 0 # keeps track of whether sample is real or fake (based off of midpoint classification)
    true_counter = 0 # counts whether the midpoint classification is right (compares classification with 5th attribute)
    false_counter = 0 # counts whether the midpoint classification is wrong

    for sublist in range(0, len(testing_data)): # classifies the attributes from testing.data
        for val in range(0, 4): # goes through the attributes of each sample
            if val == 2: # since the 3rd attribute has a different condition we address it separately (see assignment)
                if testing_data[sublist][2] <= midpoints[2]:
                    real_attr += 1
                else:
                    fake_attr += 1
            elif testing_data[sublist][val] >= midpoints[val]: # test for 1st, 2nd, 4th attribute
                fake_attr += 1
            else:
                real_attr += 1


        if fake_attr > real_attr: #sets entire sample to be real or fake based off classifier
            sample = 0.0
        elif real_attr > fake_attr:
            sample = 1.0
        elif real_attr == fake_attr: # I decided to set the sample as fake if it has equal 0, 1 attributes
            sample == 0.0

        if sample == testing_data[sublist][4]: # compares if classification matches actual value of sample
            true_counter += 1 # if classification is correct
        else:
            false_counter += 1 # if classification is wrong


        fake_attr = 0 # resets variables for next sample
        real_attr = 0
        sample = 0


    accuracy = round((true_counter / len(testing_data) * 100), 3) # accuracy calculated ( as a %) and rounded
    return accuracy # returned to main



if __name__ == '__main__': # test cases for program functionality

    print('Running trail case using "main" data...')
    midpoints = [2, 3, 1.5, 4]
    testing_data = [[2, 5, 1, 5, 0.0], [1, 1, 1, 1, 1.0], [4, 4, 3, 5, 0.0], [2, 3, 1.5, 4, 1.0],
                    [1, 4, 1, 5, 1.0]]
    accuracy = classifier(midpoints, testing_data)
    print('accuracy should be 60%, accuracy is: ', accuracy, '%')
