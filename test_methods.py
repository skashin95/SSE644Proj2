import pandas as pd
import matplotlib.pyplot as plt
from methods import calcMean, calcStdDev

arr = pd.DataFrame()

def setup():
    global arr
    url = "./female_engineer_stats.csv"
    df = pd.read_csv(url, index_col = "Year", parse_dates = False)
    arr = df.get('Percentage of Female Engineering Graduates')

    
def test_calcMean():
    mean = calcMean(arr)
    assert mean == 19.213499999999996

def test_calcStdDev():
    calcVars = calcStdDev(arr)
    assert calcVars == 1.0053450572865648
    