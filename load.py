import pandas as pd

def load_data():
    df = pd.read_csv(r"C:\Users\touqe\Prod\prod2\uber_data.csv")
    print("Data Loaded ✅")
    return df