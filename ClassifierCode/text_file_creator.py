'''Assignment 2: text_file_creator
Name: Anna Wood
Student Number: 20091785
NetID: 17aaw2'''

import urllib.request
import web_scraper

def urlToString(data_url):
    '''function that uses web_scraper to turn the webpage data into a string list.'''


    stream = urllib.request.urlopen(data_url)
    raw_data_list = web_scraper.get_all_data(stream)
    outFileCreator(raw_data_list)



def outFileCreator(money_data):
    ''''Function that creates the outfiles for  training and testing the classifier
    # need testing and training outfiles
    # even mix of real and counter samples, is split about halfway through data amont'''

    real_money = []
    counter_money = []


    for i in range(0, len(money_data)): #separates real and counterfeit money and puts them into separate lists
        val = money_data[i][0][-1]
        if val == '1':
            real_money.append(money_data[i])
        elif val == '0':
            counter_money.append(money_data[i])



    trainingFile = open("training.txt", "w+") # creates training file in a text document
    for i in range(0, int(len(real_money) / 2)):
        for val in real_money[i]:
            trainingFile.write("%s  " % val)
        trainingFile.write('\n')
    for i in range(0, int(len(counter_money) / 2)):
        for val in counter_money[i]:
            trainingFile.write("%s  " % val)
        trainingFile.write('\n')

    testingFile = open("testing.txt", "w+") # creates testing file in a text document
    for i in range(int(len(real_money) / 2), len(real_money)):
        for val in real_money[i]:
            testingFile.write(val)
        testingFile.write('\n')
    for i in range(int(len(counter_money) / 2), len(counter_money)):
        for val in counter_money[i]:
            testingFile.write( val)
        testingFile.write('\n')


    trainingFile.close()
    testingFile.close()



def floatListCreator(file):
    '''takes the data given (text document format) and returns a float list which each number as an element
    of a list, and each line of the document as a sublist of a list containing all lines. Splits numbers
    where there is a comma
    input: text document (testing.txt and training.txt for our assignment) parameter name: file
    output: float list
    '''

    file_data = [] # list for values to be added from document

    file = open(file)
    file = file.readlines()

    for val in file:  # strips line of formatting, makes each line a list  and separates each number as an index in sublist
        val = val[:-1] # takes of \n at end of string
        val = val.split(',')
        file_data.append(val)

    for i in range(0, len(file_data)):  # turns each number from string to float value
        for val in range(0, 5):
            file_data[i][val] = float(file_data[i][val])

    return file_data



if __name__ == '__main__':
    '''I decided to use the website given because I couldn't find another online text that fit 
    the requirements of my function.'''
    data_url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/00267/data_banknote_authentication.txt'
    urlToString(data_url)
    testing_txt = floatListCreator("testing.txt")
    print('test case using testing.txt and original website: \n', testing_txt)
