import requests
from datetime import datetime
import os


today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")

API_ID = ""
API_KEY = "2366fa3d20122985d6d7d4c924353007"
USER_ID = "ShoTimeSplash"
PROJECT_NM = "Workout Tracker"
SHEET_NM = "Workouts"
AGE = 25
HEIGHT_CM = 180
WEIGHT_CM = 91
GENDER = "male"


exercise_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me what exercise you did: ")

exercise_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_CM,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url=exercise_url, json=exercise_params, headers=headers)
result = response.json()
print(result)
exercise = result["exercises"][0]['name'].title()
duration = result["exercises"][0]['duration_min']
calories = result["exercises"][0]['nf_calories']

sheety_api = "https://api.sheety.co/bb05f32b81e2f3b882f0b4ba5f9ab1c5/workoutTracker/workouts"
sheet_inputs = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories,
    }
}

headers_sheety = {
    "Authorization": "Bearer 76IHXZP8d!P%839uZtiA35dKD"
}

response_sheety = requests.post(url=sheety_api, json=sheet_inputs, headers=headers_sheety)
print(response_sheety.text)
