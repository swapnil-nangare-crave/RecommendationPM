import pandas as pd

def load_data(file_path):
    """
    Loads a CSV file into a pandas DataFrame.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: The loaded DataFrame.
    """
    return pd.read_csv(file_path)

def save_data(df, file_path):
    """
    Saves a DataFrame to a CSV file.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to save.
    file_path (str): The path where the CSV file will be saved.
    """
    df.to_csv(file_path, index=False)
    
def remove_unwanted_columns(df, columns_to_remove):
    """
    Removes unwanted columns from a DataFrame.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame.
    columns_to_remove (list): List of column names to remove.
    
    Returns:
    pd.DataFrame: The DataFrame with unwanted columns removed.
    """
    return df.drop(columns=columns_to_remove)

def feature_engineering(df):
    """
    Perform feature engineering such as calculating days since last breakdown and cumulative costs.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame.
    
    Returns:
    pd.DataFrame: The DataFrame with new features.
    """
    df['Days_Since_Last_Breakdown'] = df.groupby('Equipment No.')['Breakdown Date'].diff().dt.days.fillna(0)
    df['Cumulative_Repair_Cost'] = df.groupby('Equipment No.')['Repair Cost'].cumsum()
    df['Breakdown_Frequency'] = df.groupby('Equipment No.')['Order No.'].transform('count')
    df['Cost_Ratio'] = df['Cumulative_Repair_Cost'] / df['Equip.Cost']
    
    return df

def encode_categorical_features(df, columns):
    """
    Encode categorical features in the DataFrame using Label Encoding.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame.
    columns (list): List of categorical columns to encode.
    
    Returns:
    pd.DataFrame: The DataFrame with encoded features.
    """
    from sklearn.preprocessing import LabelEncoder
    
    le = LabelEncoder()
    for col in columns:
        df[col] = le.fit_transform(df[col])
    
    return df
