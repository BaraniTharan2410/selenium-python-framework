import csv

def getCSVData(fileName):
    #create emty list to store the rows
    rows = []
    #open the csv file
    fileData = open(fileName, "r")
    #create CSV Reader from CSV file
    reader = csv.reader(fileData)
    #skip the header in CSV file
    next(reader)
    #add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows