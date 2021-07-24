'''Assignment 2: main
Name: Anna Wood
Student Number: 20091785
NetID: 17aaw2'''

import text_file_creator
import classifier_builder
import classifier

def main():
    '''this is the main interface of our program and the only location where print statements should occur.
    The program and its purpose is introduced to the user and then the accuracy of the banknote authenticator
    is shown to the user.
    Input: none (the data_url is already provided)
    output: accuracy of classifier '''
    data_url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/00267/data_banknote_authentication.txt'

    print('This is a banknote authenticity calculator...')
    print('Data of banknotes are retrieved from', data_url)
    print('A classifier determines whether each banknote is real or fake, and then')
    print('compares its decision with the actual authenticity of each note provided ')
    print('by the website. The comparisons of all notes and their original')
    print('classification is used to determine the accuracy of the banknote authenticator. \n')

    print('Program is now being run...\n')



    text_file_creator.urlToString(data_url) # creates training and testing data files

    training_data = text_file_creator.floatListCreator("training.txt")


    midpoints = classifier_builder.incomingData(training_data)


    testing_data = text_file_creator.floatListCreator("testing.txt")

    accuracy = classifier.classifier(midpoints, testing_data)
    print('Accuracy of classifier is: ', accuracy, '%')

main()

