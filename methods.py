
import pandas as pd
import matplotlib.pyplot as plt

def calcMean(arr):
    amt = arr.size
    arrSum = arr.sum()
    arrMean = arrSum/amt
    return arrMean

def calcStdDev(arr):
    mean = calcMean(arr)
    amt = arr.size
    calcVars = 0
    for index, row in df.iterrows():
        val = row['Percentage of Female Engineering Graduates']
        diff = val - mean
        calcVars = calcVars + diff**2
    return (calcVars/(amt))**0.5