import csv
import numpy as np


def getDataSource(data_path):
    Coffee_in_ml = []
    Sleep_in_hour = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Coffee_in_ml.append(float(row["Coffee in ml"]))
            Sleep_in_hour.append(float(row["sleep in hours"]))

    return {"x" :  Coffee_in_ml, "y": Sleep_in_hour}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between cup of coffee and sleep in hour :-  \n--->",correlation[0,1])

def setup():
    data_path  = "D:\projects_vansh\module3\C106\data\cupsofcoffeevshoursofsleep.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()
