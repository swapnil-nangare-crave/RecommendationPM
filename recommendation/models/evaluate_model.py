import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
import joblib

def evaluate_model():
    # Load processed data and the model
    processed_data = pd.read_csv('data/processed_data/processed_data.csv')
    model = joblib.load('models/recommendation_model.pkl')

    # Features and target
    features = ['Equip. Category', 'Maintenance Cycle', 'Equip.Cost', 'Days_Since_Last_Breakdown',
                'Cumulative_Repair_Cost', 'Breakdown_Frequency', 'Cost_Ratio']
    X = processed_data[features]
    y = processed_data['Action_Needed']

    # Predict and evaluate
    y_pred = model.predict(X)
    print("Classification Report:\n", classification_report(y, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y, y_pred))

    # Save evaluation results
    with open('models/evaluation_report/evaluation.txt', 'w') as f:
        f.write(f"Classification Report:\n{classification_report(y, y_pred)}\n")
        f.write(f"Confusion Matrix:\n{confusion_matrix(y, y_pred)}\n")
    print("Evaluation complete.")

if __name__ == "__main__":
    evaluate_model()
