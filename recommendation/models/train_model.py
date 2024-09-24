import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

def train_model():
    # Load processed data
    processed_data = pd.read_csv('data/processed_data/processed_data.csv')

    # Feature engineering: Encode categorical features
    le = LabelEncoder()
    processed_data['Equip. Category'] = le.fit_transform(processed_data['Equip. Category'])
    processed_data['Maintenance Cycle'] = le.fit_transform(processed_data['Maintenance Cycle'])

    # Define features and target
    features = ['Equip. Category', 'Maintenance Cycle', 'Equip.Cost', 'Days_Since_Last_Breakdown',
                'Cumulative_Repair_Cost', 'Breakdown_Frequency', 'Cost_Ratio']
    X = processed_data[features]
    y = processed_data['Action_Needed']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a RandomForest model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save the model
    joblib.dump(model, 'models/recommendation_model.pkl')
    print("Model training complete and saved.")

if __name__ == "__main__":
    train_model()
