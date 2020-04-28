"""Written by Nognut"""
#!/usr/local/bin/python3.8
"""
    This program will read the CRON errors from sample.log files and will make a new report.log file
"""
import sys
import re

"""a function to search for the error(s)"""
def search_errors(log_file):
    input_error = input("Enter the error type: ")#inputing type of ERROR
    returned_errors = []
    with open(log_file, mode='r', encoding='UTF-8') as file:#opening file in read mode with UTF-8 encoding.
        for log in file.readlines():
            error_patterns_list = []#for filtering out 'ERROR' logs only and can be changed to other error types such as 'INFO' and 'WARN' or 'USER'.
            #it can also can be also initialized empty to fetch all types of logs, irrespective of their type.
            for i in range(len(input_error.split(' '))):
                error_patterns_list.append(r"{}".format(input_error.split(' ')[i].lower()))#adding lines to the list.
            for error_patterns in error_patterns_list:
                if re.search(error_patterns, log.lower()):
                    returned_errors.append(log)#appending to the list.
        file.close()
    return returned_errors

"""a function to create an output ERROR_report.log file"""
def output_file(returned_errors):
    with open('ERROR_reports.log', 'w') as file:
        #"""The actual log file and the report file are in the same directory. If in a different directory, then you can use a full path name"""
        for e in returned_errors:
            file.write(e)
        print("ERROR_report.log file has been created")
        file.close()

"""the main function"""
if __name__ == "__main__":
    log_file = sys.argv[1]#input the log file name while running the script
    returned_errors = search_errors(log_file)#fetching the errors
    output_file(returned_errors)#saving on to report.log file
    sys.exit(0)#exiting normally
