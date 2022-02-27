import csv
import numpy as np


def getDataSource(data_path):
    percentage_marks = []
    present_days = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            percentage_marks.append(float(row["Percentage of Marks"]))
            present_days.append(float(row["Present Days"]))

    return {"x" : percentage_marks, "y": present_days}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Percentage of Marks and Present days :-  \n--->",correlation[0,1])

def setup():
    data_path  = "./data/Student Marks vs Days Present.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()
