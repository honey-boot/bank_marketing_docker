# Bank Churn Prediction Web App

This project is a Machine Learning-powered web app built using Streamlit and Docker. It predicts whether a customer will churn from a bank based on various attributes.

## 🚀 Features
- Streamlit Web Interface
- Dockerized Deployment
- Logistic Regression Model (or your model)
- Real-time predictions

## 🐳 Run with Docker

```bash
docker pull thenmozhidharma12345/bank-churn-app:latest
docker run -p 8501:8501 thenmozhidharma12345/bank-churn-app
Open your browser at http://localhost:8501

🧠 ML Model
The model was trained using LogisticRegression on cleaned bank marketing data.
The .pkl file is loaded in the Streamlit app for inference.

📁 Project Structure
Copy
Edit
├── app.py
├── Dockerfile
├── requirements.txt
├── model.pkl
├── bank.ipynb
└── README.md
🛠 Requirements
Install using:

bash
Copy
Edit
pip install -r requirements.txt
📷 Screenshots
![image](https://github.com/user-attachments/assets/ff58bb32-3523-4bf1-acef-35d36323ed35)
![image](https://github.com/user-attachments/assets/e4f6d307-2a99-4bc3-9cfa-decee7f699b3)

👩‍💻 Author
Thenmozhi Dharma
Docker Hub | GitHub

yaml
Copy
Edit

---

### 📤 Steps to Push to GitHub

1. Create a new GitHub repo (e.g., `bank-churn-docker-streamlit`)
2. Initialize git (if not already):
```bash
git init
git remote add origin https://github.com/yourname/repo-name.git
Add and push files:

bash
Copy
Edit
git add .
git commit -m "Initial commit for Dockerized bank churn app"
git push -u origin main
