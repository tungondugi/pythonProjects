#!/usr/bin/python

#importing the required modules
import re
import operator
import csv
import sys

__author__ = "Nognut"

#The data_generator function takes an arguement which is a syslog file.
#It returns a tuple of two sorted dictionary which are itself a tuple.
# The function calculates the 1.) Number of INFO and ERROR of a username; 2.) Total count of each Error messages.
#-----------------------------------------------------------start of the function------------------------------------------------------------
def data_generator(logfile):
    with open(logfile, mode='r') as infile:
        data = infile.readlines()
        #defining two empty dictionary
        error_dict = dict()  # for number of error msgs
        user_dict = dict()  # for the number of users

        # matching all the error messages.
        error_pattern = r"ticky: ERROR ([\w].+ )"
        # matching all the usernames.
        user_pattern = r"\(([\w].+)\)"
        for line in data:
            #for info_dict
            #the following lines calculates the Number of INFO and ERROR of a username;
            #--------------------start------------------------
            user_result = re.search(user_pattern, line)
            if user_result != None:
                if "INFO" in line:
                    if user_result[1] in user_dict:
                        # if present increment by 1
                        user_dict[user_result[1]][0] += 1
                    else:
                        # if not present add the item
                        user_dict[user_result[1]] = [1, 1]
                if "ERROR" in line:
                    if user_result[1] in user_dict:
                        # if present increment by 1
                        user_dict[user_result[1]][1] += 1
                    else:
                        # if not present add the item
                        user_dict[user_result[1]] = [1, 1]
            #------------------end------------------------------
            #for error_dict
            #the following lines calculates the Total count of each Error messages.
            #--------------------start------------------------
            error_result = re.search(error_pattern, line)
            if error_result != None:
                if error_result[1] in error_dict:
                    error_dict[error_result[1]] += 1  # if present increment by 1.
                else:
                    error_dict[error_result[1]] = 1  # if not present add the item.
            #------------------end------------------------------

        #sorting the dictionaries.
        userDict = sorted(user_dict.items())  # sorting according to the key
        errDict = sorted(error_dict.items(), key=operator.itemgetter(1), reverse=True)  # sorting according to the value
        
        return (userDict, errDict) #returning as a tuple
#------------------------------------------------------------end of the function-------------------------------------------------------------

#The gen_error_csv function takes exactly one arguement which is the sorted error dictionary(tuple) returned from the above function.
#It generates an HTML page called error_message.csv
#-----------------------------------------------------------start of the function------------------------------------------------------------
def gen_error_csv(errDict):
    """creating error_message.csv file"""
    with open("error_message.csv", mode="w", newline="") as errFile:
        #here the newline='' removes the extra blank line
        errWriter = csv.writer(errFile)
        errWriter.writerow(["Error", "Count"])#heading of the file
        for row in errDict:
            errWriter.writerow(row)
#------------------------------------------------------------end of the function----------------------------------------------------------------

#The gen_user_csv function takes exactly one arguement which is the sorted user dictionary(tuple) returned from the above function.
#It generates an HTML page called error_message.csv
#-----------------------------------------------------------start of the function------------------------------------------------------------
def gen_user_csv(userDict):
    """creating user_statitics.csv file"""
    with open("user_statistics.csv", mode="w", newline="") as userfile:
        #here the newline='' removes the extra blank line
        userWriter = csv.writer(userfile)
        userWriter.writerow(["Username","INFO", "ERROR"])#heading of the file
        for key, value in userDict:
            data_list = [key,value[0],value[1]]
            userWriter.writerow(data_list)
#------------------------------------------------------------end of the function----------------------------------------------------------------


#the main Functions
if __name__ == "__main__":
    logfilename = sys.argv[1]

    #Indexed because data_generator(logfilename) function returns a tuple with two elements
    userDict = data_generator(logfilename)[0]
    errDict = data_generator(logfilename)[1]

    #finally generating the HTML files(reports).
    gen_user_csv(userDict)
    gen_error_csv(errDict)
