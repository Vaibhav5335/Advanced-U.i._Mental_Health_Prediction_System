from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.conf import settings
import pandas as pd
import numpy as np
import joblib
import os
from .models import PredictionResult
import django
django.setup()

def welcome(request):
    return render(request, 'welcome.html')

def register_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']


        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return render(request, 'register.html')


        user = User.objects.create(
            first_name=name,
            username=username,
            password=make_password(password)
        )
        messages.success(request, 'Registration successful! Please login.')
        return redirect('login')

    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Login Failed')

    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('welcome')

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def predict_view(request):
    if request.method == 'POST':
        try:

            gender = request.POST['gender']
            sleep_hours = float(request.POST['sleep_hours'])
            study_hours = float(request.POST['study_hours'])
            meals_per_day = int(request.POST['meals_per_day'])
            social_media_hours = float(request.POST['social_media_hours'])
            physical_activity_hours = float(request.POST['physical_activity_hours'])
            substance_use = request.POST['substance_use']
            academic_percentage = float(request.POST['academic_percentage'])



            gender_encoded = 1 if gender.lower() == 'male' else 0
            substance_use_encoded = 1 if substance_use.lower() == 'yes' else 0


            features = np.array([[
                gender_encoded,
                sleep_hours,
                study_hours,
                meals_per_day,
                social_media_hours,
                physical_activity_hours,
                substance_use_encoded,
                academic_percentage
            ]])


            scaler_path = os.path.join(settings.ML_MODELS_DIR, 'scaler_model.pkl')
            model_path = os.path.join(settings.ML_MODELS_DIR, 'health_model.pkl')

            scaler = joblib.load(scaler_path)
            model = joblib.load(model_path)


            features_scaled = scaler.transform(features)


            prediction = model.predict(features_scaled)[0]
            prediction_proba = model.predict_proba(features_scaled)[0]


            categories = ['Healthy', 'Moderately Affected', 'Severely Affected']
            predicted_category = categories[prediction]
            confidence = max(prediction_proba) * 100


            PredictionResult.objects.create(
                user=request.user,
                gender=gender,
                sleep_hours=sleep_hours,
                study_hours=study_hours,
                meals_per_day=meals_per_day,
                social_media_hours=social_media_hours,
                physical_activity_hours=physical_activity_hours,
                substance_use=substance_use,
                academic_percentage=academic_percentage,
                predicted_category=predicted_category
            )


            request.session['prediction_result'] = {
                'category': predicted_category,
                'confidence': round(confidence, 2)
            }

            return redirect('result')

        except Exception as e:
            messages.error(request, f'Error in prediction: {str(e)}')

    return render(request, 'predict.html')

@login_required
def result_view(request):
    result = request.session.get('prediction_result')
    if not result:
        return redirect('predict')

    return render(request, 'result.html', {'result': result})

def test_model_loading():
    """Test if the ML models can be loaded and used for prediction"""

    try:

        scaler_path = os.path.join(settings.ML_MODELS_DIR, 'scaler_model.pkl')
        model_path = os.path.join(settings.ML_MODELS_DIR, 'health_model.pkl')

        print("Testing model loading...")
        print(f"Scaler path: {scaler_path}")
        print(f"Model path: {model_path}")


        if not os.path.exists(scaler_path):
            print(f"❌ Error: scaler_model.pkl not found at {scaler_path}")
            return False

        if not os.path.exists(model_path):
            print(f"❌ Error: health_model.pkl not found at {model_path}")
            return False


        print("Loading scaler...")
        scaler = joblib.load(scaler_path)
        print("✅ Scaler loaded successfully!")

        print("Loading model...")
        model = joblib.load(model_path)
        print("✅ Model loaded successfully!")


        print("\nTesting prediction with sample data...")


        sample_features = np.array([[
            1,
            7.5,
            5.0,
            3,
            2.5,
            1.0,
            0,
            85.5
        ]])

        print(f"Sample input shape: {sample_features.shape}")
        print(f"Sample input: {sample_features[0]}")


        features_scaled = scaler.transform(sample_features)
        print(f"Scaled features: {features_scaled[0]}")


        prediction = model.predict(features_scaled)[0]
        prediction_proba = model.predict_proba(features_scaled)[0]


        categories = ['Healthy', 'Moderately Affected', 'Severely Affected']
        predicted_category = categories[prediction]
        confidence = max(prediction_proba) * 100

        print(f"\n🎯 Prediction Result:")
        print(f"   Category: {predicted_category}")
        print(f"   Confidence: {confidence:.2f}%")
        print(f"   Raw prediction: {prediction}")
        print(f"   Probabilities: {prediction_proba}")

        print("\n✅ All tests passed! Your models are ready to use.")
        return True

    except Exception as e:
        print(f"❌ Error during testing: {str(e)}")
        print("\nTroubleshooting tips:")
        print("1. Make sure both model files are in the ml_models/ directory")
        print("2. Check that the file names are exactly 'scaler_model.pkl' and 'health_model.pkl'")
        print("3. Ensure the models were trained with the same feature order")
        return False

if __name__ == "__main__":
    test_model_loading()