import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

def clean_data(df):
    df = df.dropna()
    df['Gender'] = df['Gender'].map({'Female': 0, 'Male': 1})
    return df

def engineer_features(df):
    df['BalanceSalaryRatio'] = df['Balance'] / (df['EstimatedSalary'] + 1)
    return df

def etl(filepath):
    df = load_data(filepath)
    df = clean_data(df)
    df = engineer_features(df)
    return df
