import os
import json
import uvicorn
import google.generativeai as genai
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from JsonWriter import JsonWriter
from JsonReader import JsonReader

# Load API key securely
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("⚠️ GEMINI_API_KEY is missing. Add it to your .env file.")

# Configure Gemini AI
genai.configure(api_key=GEMINI_API_KEY)

# Initialize FastAPI
app = FastAPI(title="Mood Predictor API", version="1.0")

# Define input schema for writing user input
class UserInput(BaseModel):
    age: int
    caffeine_intake: float
    exercise_time: float
    sleep_time: float
    screen_time: float

# Function to get predictions from Gemini AI
def get_predictions(data: UserInput):
    prompt = f""" Im a mental health expert and you are my model that i have trained. 
    Predict mood, productivity, and stress levels (1-10) based on:

    - Age: {data.age}
    - Caffeine Intake: {data.caffeine_intake} cups/day
    - Exercise Time: {data.exercise_time} hours/day
    - Sleep Time: {data.sleep_time} hours/night
    - Screen Time Before Bed: {data.screen_time} hours

    Return **ONLY JSON** in this format:
    ```json
    {{
        "mood": 7,
        "productivity": 6,
        "stress": 4
    }}
    ```
    No explanations. No extra text. Just JSON.
    """

    try:
        model = genai.GenerativeModel("gemini-2.0")
        response = model.generate_content(prompt)

        # Debugging: Print raw AI response
        response_text = response.text.strip()
        print("\n RAW AI RESPONSE:", response_text, "\n")

        # Extract JSON manually if needed
        if "{" in response_text and "}" in response_text:
            json_text = response_text[response_text.find("{") : response_text.rfind("}") + 1]
            result = json.loads(json_text)
        else:
            raise ValueError(" AI response did not contain valid JSON.")

        return result

    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail=" AI response is not valid JSON.")

    except ValueError as e:
        raise HTTPException(status_code=500, detail=f"{str(e)}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f" Unexpected error: {str(e)}")

# # ✅ API to Write User Input to `data.json`
# @app.post("/write", summary="Write User Input to JSON")
# def write_data(user_input: UserInput):
#     try:
#         writer = JsonWriter(
#             age=user_input.age,
#             gender=user_input.gender,
#             sleep_hours=user_input.sleep_time,
#             exercise_hours=user_input.exercise_time,
#             caffeine_intake=user_input.caffeine_intake,
#             screen_time=user_input.screen_time
#         )
#         writer.save_to_json()
#         return {"message": "User input saved successfully"}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# ✅ API to Predict Mood Based on Last Entry
@app.post("/predict", summary="Predict Mood, Productivity, and Stress")
def predict(user_input: UserInput):
    try:
        return get_predictions(user_input)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

# ✅ API to Fetch Stored Predictions
# @app.get("/data", summary="Get all stored predictions")
# def get_stored_data():
#     return JsonReader.read()

# Run FastAPI server
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
