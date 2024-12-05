import pandas as pd

def addcolumns(df):
    df["Serial"] = df["Serial"].astype(str)
    df["日期"] = pd.to_datetime(df["Serial"].str.slice(0,8))
    df["時間"] = df["Serial"].str.slice(8,10)
    df["時段"] = df["Serial"].str.slice(10,12)
    df["位置"] = df["Serial"].str.slice(12,14)
    return(df)
if __name__=="__main__":
    pass

