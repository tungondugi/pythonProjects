#!/usr/bin/python

import sys

__author__ = "Nognut"

# Run as: ./csv_to_html.py <input csv file name> <report file name>
# The script requires 2 arguements: the input file name and the generated file name.
# It expects a CSV file as an input to parse into an html table,
# and assumes that the column headers are located in the first row.
#------------------------start of the function----------------------------
def generate_HTML_report(csvFilename, reportFilename):
    with open(csvFilename, mode='r') as infile:
        data = infile.readlines()

        #for writing into the file.
        with open(reportFilename, mode="w") as outfile:

            #stylings to give border to the table elements
            styles = """
            <style >
                table, th, td{
                    border: 1px solid black;
                    border-collapse: collapse;
                }
                th, td{
                    padding: 5px ;
                    text-align: left;
                }
            </style >
            """
            #color scheme for the table.
            tr_style = "background-color:rgb(206,202,202);"
            table_style = "width:50%;background-color:rgb(124,197,197);"

            #opening tag of the table;
            table = "<table>\n"

            #creating the table headers.
            header = data[0].split(",")

            """writing the heading elements"""
            table += " <tr style={}>\n".format(
                table_style)  # opening tag for table row
            for cols in header:
                # writing the headings
                table += "  <th style={}>{}</th>\n".format(tr_style, cols.strip())
            table += " </tr>\n"  # closing tag for the table row

            """writing the other row elements"""
            for cols in data[1:]:
                # opening tag for table row
                table += " <tr style={}>\n".format(table_style)
                lines = cols.split(",")
                for line in lines:
                    table += "  <td>{}</td>\n".format(line.strip())
                table += " </tr>\n"  # closing tag for the table row

            #this is the closing tag of the table
            table += "</table>"

            """finally writing into the file"""
            outfile.write(styles)
            outfile.write(table)

            #closing the file objects (these fields are optional.)
            infile.close()
            outfile.close()
#------------------------------------------------------------end of the function----------------------------------------------------------------

#the main functions
if __name__ == "__main__":

    csvFilename = sys.argv[1]#for the csv file
    genFilename = sys.argv[2]#for generated html file

    #calling the function
    generate_HTML_report(csvFilename, genFilename)
