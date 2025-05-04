# wisconsin-breast-cancer

🧠 Breast Cancer Classification with PostgreSQL & Streamlit

A locally run machine learning project for breast cancer detection using the Wisconsin Breast Cancer Dataset.
Data is stored in a PostgreSQL database and regularly extended. A Python-based model performs classification, and results are displayed through a simple Streamlit web app.

# 📌 Who Is This For?
This project is ideal for:

- Medical professionals, researchers, or data enthusiasts (even in rural or local settings)
- Solo developers or small teams without cloud infrastructure
- Anyone who prefers to work locally on their laptop or workstation

# ⚙️ Technologies Used
Python 3.x
PostgreSQL (local or LAN setup)
Pandas, scikit-learn, psycopg2, SQLAlchemy
Streamlit (for a simple web UI)

# 🧰 Requirements
Python is installed (recommended via Anaconda or python.org)
PostgreSQL is installed and running locally
Internet access is only required for setup (e.g., installing Python packages)

# 🛠️ Installation & Getting Started
## Clone the project
git clone https://github.com/your-username/your-repo.git
cd your-repo
## Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
## Install required packages
pip install -r requirements.txt
## Set up PostgreSQL database
Start PostgreSQL (via pgAdmin or terminal)
## Create a new database, e.g., breast_cancer
Configure connection settings in config.py or .env, for example:
DB_NAME = "breast_cancer"
DB_USER = "postgres"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_PORT = "5432"
## Start the Streamlit app
streamlit run app.py
## (Optional) Run the data updater script
You can run it manually or schedule it (e.g., via cron or Windows Task Scheduler):
python data_updater.py
## 🧠 What This Project Does
Uses the well-known Wisconsin Breast Cancer Dataset
Stores all data persistently in PostgreSQL
Trains a classification model (e.g., Random Forest, SVM)
Provides an interactive Streamlit interface for viewing predictions
Keeps itself updated with fresh data using an external Python script

# 🗂️ Project Structure

## 📂 Repository Structure
```

├── app.py               # Streamlit web app
├── data_updater.py      # Script to add new data
├── ml_model.py          # Machine learning logic
├── database.py          # DB connections and table management
├── config.py / .env     # DB credentials
├── requirements.txt     # Required Python packages
└── README.md

```

## 📈 Future Improvements
Automatically re-train the model when new data is added
Allow users to upload CSVs via the web interface
Deploy the Streamlit app within a local network (e.g., small clinic or lab)
