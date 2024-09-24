import pandas as pd

def preprocess_data():
    # Load raw data
    raw_data = pd.read_csv('data/raw_data/raw_maintenance_data.csv')

    # Remove any unwanted characters from cost columns
    raw_data['Repair Cost'] = raw_data['Currency'].str.rstrip('$').astype('int')
    raw_data['Equip.Cost'] = raw_data['Equip.Cost'].str.rstrip('$').astype('int')

    # Remove unnecessary columns
    processed_data = raw_data.drop(columns=['Currency', 'Unnamed: 5', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10'])

    # Create new features: Days since last breakdown, Cumulative repair cost, etc.
    processed_data['Days_Since_Last_Breakdown'] = processed_data.groupby('Equipment No.')['Breakdown Date'].diff().dt.days.fillna(0)
    processed_data['Cumulative_Repair_Cost'] = processed_data.groupby('Equipment No.')['Repair Cost'].cumsum()
    processed_data['Breakdown_Frequency'] = processed_data.groupby('Equipment No.')['Order No.'].transform('count')
    processed_data['Cost_Ratio'] = processed_data['Cumulative_Repair_Cost'] / processed_data['Equip.Cost']

    # Save processed data
    processed_data.to_csv('data/processed_data/processed_data.csv', index=False)
    print("Data preprocessing complete.")

if __name__ == "__main__":
    preprocess_data()
