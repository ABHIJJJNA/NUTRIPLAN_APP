# Nutriplan: Generative AI in Personalized Nutrition Planning

## 🌟 Project Overview
Nutriplan is a cutting-edge application designed to provide personalized nutrition plans and analyze food images for calorie content using Generative AI. Powered by the Gemini AI model and built with Streamlit, Nutriplan serves as a personal nutritionist, helping users make informed dietary choices.

---

## 🛠️ Features
- Personalized Meal Plan Generator: 
  Generate meal plans tailored to individual user needs, including age, weight, height, and dietary preferences.
  
- Calorie Analysis from Images 
  Upload images of meals, and the application estimates the calorie content using AI.

- Interactive User Interface: 
  A simple and intuitive interface built with Streamlit for user-friendly interactions.

---

## ⚙️ Project Architecture
1. Frontend (Streamlit): 
   - Collects user input and displays results.
   - Handles image uploads and meal plan generation.

2. Backend (Python): 
   - Processes user data and uses the Gemini AI API to generate results.
   - Implements the random greedy algorithm for meal planning.

3. Generative AI (Gemini API):
   - Uses the Gemini AI model for analyzing images and generating creative responses.

---

## 🚀 How to Run the Project
### Prerequisites
- Python 3.11 or higher
- Required Python libraries (listed in `requirements.txt`)
- An API key for Gemini AI (set as an environment variable)

### Setup Instructions
1. Clone the Repository:
   ```bash
   git clone <repository_url>
   cd Nutriplan


## Create a Virtual Environment:
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

## Install Dependencies:
    pip install -r requirements.txt
    Set Up Environment Variables:

## Set Up Environment Variables:
  ### Create a .env file in the project root with the following content:
    GEMINI_API_KEY=your_api_key_here
  Replace your_api_key_here with your actual Gemini AI API key.
  
## Run the Application:
    streamlit run app.py
Open your browser and navigate to the provided localhost URL.

🧩 Folder Structure
bash
Copy code
Nutriplan/
│
├── app.py                # Main Streamlit application
├── api_key.py            # (Removed for security; use .env for keys)
├── requirements.txt      # Python dependencies
├── .gitignore            # Ignored files and folders
├── .env                  # Environment variables (not tracked by Git)
└── README.md             # Project documentation

📜 Usage Instructions
Generate a Meal Plan:

Enter your age, weight, height, and dietary preferences.
Click "Generate Meal Plan" to get a personalized plan.
Analyze Food Images:

Upload a photo of your meal.
Click "Analyze Image" to estimate its calorie content.


💻 Technologies Used
Programming Language: Python
Framework: Streamlit
Generative AI API: Gemini AI
Image Processing: PIL (Python Imaging Library)
Environment Management: Python-dotenv

📈 Future Enhancements
Add support for multiple AI models for calorie analysis.
Enable saving meal plans and calorie data for long-term tracking.
Integrate fitness recommendations based on user goals.

🛡️ Security Practices
API keys are stored in environment variables and excluded from the repository using .gitignore.
Follow best practices for secret management.

🤝 Contributions
Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.


---

### Key Notes:
- Replace placeholders like `<repository_url>`, `your_api_key_here`, and `your_email@example.com` with actual details.
- Add more information if your project includes unique features or improvements over time.

Let me know if you'd like to customize any section further!


