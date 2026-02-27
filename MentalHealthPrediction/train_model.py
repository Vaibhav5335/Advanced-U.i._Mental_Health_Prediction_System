import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

def train_mental_health_model():
    """
    Train mental health prediction model and save scaler and model separately
    """


    try:
        df = pd.read_excel('Cleaned_data.xlsx')
        print("Dataset loaded successfully!")
        print(f"Dataset shape: {df.shape}")
        print(f"Columns: {list(df.columns)}")
    except FileNotFoundError:
        print("Cleaned_data.xlsx not found. Creating sample data...")

        np.random.seed(42)
        n_samples = 1000

        df = pd.DataFrame({
            'Gender': np.random.choice(['Male', 'Female'], n_samples),
            'Sleep_Hours': np.random.normal(7, 1.5, n_samples),
            'Study_Hours': np.random.normal(4, 2, n_samples),
            'Meals_Per_Day': np.random.randint(1, 5, n_samples),
            'Social_Media_Hours': np.random.normal(3, 1.5, n_samples),
            'Physical_Activity_Hours': np.random.normal(1, 0.5, n_samples),
            'Substance_Use': np.random.choice(['Yes', 'No'], n_samples, p=[0.3, 0.7]),
            'Academic_Percentage': np.random.normal(75, 15, n_samples),
        })


        conditions = []
        for i in range(len(df)):
            score = 0

            if df.iloc[i]['Sleep_Hours'] < 6 or df.iloc[i]['Sleep_Hours'] > 9:
                score += 1

            if df.iloc[i]['Study_Hours'] > 8 or df.iloc[i]['Study_Hours'] < 2:
                score += 1

            if df.iloc[i]['Social_Media_Hours'] > 4:
                score += 1

            if df.iloc[i]['Physical_Activity_Hours'] < 0.5:
                score += 1

            if df.iloc[i]['Substance_Use'] == 'Yes':
                score += 1

            if df.iloc[i]['Academic_Percentage'] < 60:
                score += 1

            if score <= 1:
                conditions.append('Healthy')
            elif score <= 3:
                conditions.append('Moderately Affected')
            else:
                conditions.append('Severely Affected')

        df['Mental_Health_Status'] = conditions
        print("Sample dataset created!")



    le_gender = LabelEncoder()
    le_substance = LabelEncoder()
    le_target = LabelEncoder()

    df['Gender_Encoded'] = le_gender.fit_transform(df['Gender'])
    df['Substance_Use_Encoded'] = le_substance.fit_transform(df['Substance_Use'])


    feature_columns = [
        'Gender_Encoded', 'Sleep_Hours', 'Study_Hours', 'Meals_Per_Day',
        'Social_Media_Hours', 'Physical_Activity_Hours', 'Substance_Use_Encoded', 'Academic_Percentage'
    ]

    X = df[feature_columns].values
    y = le_target.fit_transform(df['Mental_Health_Status'])


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)


    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)


    y_pred = model.predict(X_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=le_target.classes_))


    os.makedirs('ml_models', exist_ok=True)


    joblib.dump(scaler, 'ml_models/scaler_model.pkl')
    joblib.dump(model, 'ml_models/health_model.pkl')


    joblib.dump(le_target, 'ml_models/label_encoder.pkl')

    print("\nModels saved successfully!")
    print("- scaler_model.pkl: Feature scaler")
    print("- health_model.pkl: Mental health classifier")
    print("- label_encoder.pkl: Target label encoder")

    return model, scaler, le_target

if __name__ == "__main__":
    train_mental_health_model()