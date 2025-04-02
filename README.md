# Flask API Project

A simple Flask API project with `.env` configuration and separated business logic using a service layer.

---

## 📌 Features

- ✅ API Routes with Flask
- ✅ Environment variable management using `python-dotenv`
- ✅ Business logic separated using service files
- ✅ Structured and scalable project layout

---

## 📂 Project Structure
face-recognition/ │ ├── venv/ # Virtual environment directory ├── app/ │ ├── init.py │ ├── routes.py │ ├── services/ │ │ └── hello_service.py ├── .env ├── requirements.txt ├── config.py ├── app.py └── README.md


Create a virtual environment and activate it
python3 -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate



Install dependencies
pip install -r requirements.txt



Create a .env file
FLASK_ENV=development
SECRET_KEY=your_secret_key


Run the application
python app.py
