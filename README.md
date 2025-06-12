AI Climate Forecasting App
📌 Overview
This project is an AI-powered climate forecasting application that integrates ERA5 climate data and machine learning to predict environmental trends. Built with Flask, it serves as an API that processes climate data and delivers insights.

🛠 Tech Stack
Backend: Flask, Flask-CORS, Gunicorn

Machine Learning: TensorFlow, Scikit-Learn, LSTM models

Data Processing: Pandas, Requests, ECMWF CDS API

Deployment: Render, GitHub Actions

Visualization: Chart.js (for frontend insights)

🚀 Setup & Installation
1️⃣ Clone the repository
bash
git clone https://github.com/mwangiasford1/ai-climate-app.git
cd ai-climate-app
2️⃣ Create & Activate Virtual Environment
bash
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate  # Windows
3️⃣ Install Dependencies
bash
pip install -r requirements.txt
4️⃣ Run the Application
bash
python webapp/app.py
🌍 Deployment on Render
To deploy, push the latest changes to GitHub and let Render handle the deployment:

bash
git add .
git commit -m "Updated climate forecasting model"
git push origin main
Render automatically pulls updates and rebuilds the service.

🔗 API Endpoints
/predict → Returns AI-powered climate forecasts

/data → Retrieves ERA5 processed climate data

/healthcheck → Confirms API status

📩 Contributions
Feel free to contribute by:

Forking the repository

Creating a feature branch

Submitting a pull request

📜 License
This project is licensed under MIT License.
