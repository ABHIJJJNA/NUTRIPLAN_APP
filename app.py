import streamlit as st
import requests
from PIL import Image
import io
import google.generativeai as genai

from api_key import gemini_api_key

# Configure the API key for Gemini
genai.configure(api_key=gemini_api_key)

# Function to analyze food image using Gemini AI for calorie content
def analyze_food_image(image_data):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content([
            "Analyze this food image and provide calorie content.",
            {"mime_type": "image/jpeg", "data": image_data}
        ])
        return response.text.strip()
    except Exception as e:
        st.error(f"Error analyzing food image: {e}")
        return None

# Function to generate personalized meal plan based on user data
def generate_meal_plan(age, weight, height, dietary_needs):
    prompt = f"Create a personalized meal plan for a {age}-year-old person weighing {weight} kg and {height} cm tall with dietary needs: {dietary_needs}."
    try:
        response = genai.GenerativeModel('gemini-1.5-flash').generate_content([prompt])
        return response.text.strip()
    except Exception as e:
        st.error(f"Error generating meal plan: {e}")
        return None

# Streamlit app frontend setup
st.set_page_config(page_title="AI Diet Planner", page_icon=":apple:")
st.title("AI Diet Planner")
st.subheader("Your personal nutritionist powered by Gemini AI")

# User input for personal data
age = st.number_input("Enter your age:", min_value=1, max_value=120)
weight = st.number_input("Enter your weight (kg):", min_value=1.0)
height = st.number_input("Enter your height (cm):", min_value=1)
dietary_needs = st.text_input("Enter any dietary needs or restrictions:")

# Image upload section for calorie analysis
uploaded_file = st.file_uploader("Upload an image of your meal:", type=["png", "jpg", "jpeg"])

if st.button("Analyze Image"):
    if uploaded_file is not None:
        image_data = uploaded_file.read()
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
        
        # Analyze food image for calorie content
        calorie_info = analyze_food_image(image_data)
        
        if calorie_info:
            st.success(f"Calorie information: {calorie_info}")

if st.button("Generate Meal Plan"):
    if age and weight and height:
        meal_plan = generate_meal_plan(age, weight, height, dietary_needs)
        
        if meal_plan:
            st.subheader("Your Personalized Meal Plan:")
            st.write(meal_plan)
    else:
        st.warning("Please fill in all personal data fields to generate a meal plan.")