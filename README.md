# wisconsin-breast-cancer
Wisconsin Breast Cancer

🧠 Wisconsin Breast Cancer Classifier

Ein Machine-Learning-Projekt zur Klassifikation von Brustkrebsdaten aus dem Wisconsin Breast Cancer Dataset. Es nutzt eine PostgreSQL-Datenbank zur Speicherung und kontinuierlichen Erweiterung des Datensatzes sowie eine Streamlit-Oberfläche zur Visualisierung der Ergebnisse.

📁 Inhaltsverzeichnis
Überblick
Verwendete Technologien
Setup & Installation
Verwendung
Projektstruktur
Zukünftige Erweiterungen
🔍 Überblick
Dieses Projekt automatisiert die Analyse und Klassifikation des Wisconsin Breast Cancer Dataset mit folgenden Hauptfunktionen:

Speicherung der Daten in einer PostgreSQL-Datenbank
Ein Python-Skript, das den Datensatz regelmäßig um neue Daten erweitert
Ein ML-Modell zur Klassifikation (z. B. mittels Random Forest, SVM o.ä.)
Eine interaktive Streamlit-App, um Vorhersagen und Statistiken anzuzeigen
🛠️ Verwendete Technologien
🐍 Python 3.x
🧮 PostgreSQL
📦 Pandas, scikit-learn, SQLAlchemy
📊 Streamlit
📡 psycopg2 (PostgreSQL-Anbindung)
⚙️ Setup & Installation
Repository klonen
git clone https://github.com/dein-nutzername/dein-repo.git
cd dein-repo
Python-Umgebung erstellen (optional)
python -m venv venv
source venv/bin/activate  # oder venv\Scripts\activate (Windows)
Abhängigkeiten installieren
pip install -r requirements.txt
Datenbank einrichten
Erstelle eine PostgreSQL-Datenbank und passe die Verbindungsdaten in der Datei config.py oder .env an.
Streamlit starten
streamlit run app.py
▶️ Verwendung
Die Streamlit-App zeigt Metriken, Visualisierungen und erlaubt neue Klassifikationen.
Das Python-Skript (data_updater.py) erweitert regelmäßig die Datenbank.
Das Modell wird regelmäßig mit aktualisierten Daten trainiert.
🗂️ Projektstruktur
.
├── app.py               # Streamlit-Oberfläche
├── data_updater.py      # Fügt neue Daten hinzu
├── ml_model.py          # ML-Training und Klassifikation
├── database.py          # Verbindung zu PostgreSQL
├── config.py            # Konfiguration der Datenbankverbindung
├── requirements.txt     # Python-Abhängigkeiten
└── README.md
🌱 Zukünftige Erweiterungen
Automatisiertes Retraining bei neuen Daten
Deployment der App (z. B. über Streamlit Cloud oder Heroku)
Einbindung von Benutzer-Uploads für eigene Vorhersagen
