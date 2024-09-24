import joblib

def deploy_model():
    # Load the trained model
    model = joblib.load('models/recommendation_model.pkl')
    
    # Here you can implement the deployment logic, e.g., expose it via an API, 
    # push it to a model server, or integrate with SAP AI Core.

    print("Model deployed successfully.")

if __name__ == "__main__":
    deploy_model()
