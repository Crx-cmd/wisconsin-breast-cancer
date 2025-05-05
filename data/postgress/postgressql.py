import pandas as pd
import psycopg2

# CSV-Datei einlesen
df = pd.read_csv("/Users/heinerploog/Desktop/Github/wisconsin-breast-cancer/data/data.csv")

df = df[['diagnosis', 'radius_mean', 'texture_mean', 'perimeter_mean',
       'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean',
       'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
       'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
       'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
       'fractal_dimension_se', 'radius_worst', 'texture_worst',
       'perimeter_worst', 'area_worst', 'smoothness_worst',
       'compactness_worst', 'concavity_worst', 'concave points_worst',
       'symmetry_worst', 'fractal_dimension_worst']]

# Verbindung zur PostgreSQL-Datenbank herstellen
conn = psycopg2.connect(
    dbname="heinerploog", 
    user="heinerploog", 
    password="hamburg1", 
    host="localhost", 
    port="5432"
)
cur = conn.cursor()

# Tabelle erstellen (falls noch nicht vorhanden)
cur.execute("""
    CREATE TABLE IF NOT EXISTS wisconsin.patients (
        id SERIAL PRIMARY KEY,
        diagnosis TEXT,
        radius_mean DOUBLE PRECISION,
        texture_mean DOUBLE PRECISION,
        perimeter_mean DOUBLE PRECISION,
        area_mean DOUBLE PRECISION,
        smoothness_mean DOUBLE PRECISION,
        compactness_mean DOUBLE PRECISION,
        concavity_mean DOUBLE PRECISION,
        concave_points_mean DOUBLE PRECISION,
        symmetry_mean DOUBLE PRECISION,
        fractal_dimension_mean DOUBLE PRECISION,
        radius_se DOUBLE PRECISION,
        texture_se DOUBLE PRECISION,
        perimeter_se DOUBLE PRECISION,
        area_se DOUBLE PRECISION,
        smoothness_se DOUBLE PRECISION,
        compactness_se DOUBLE PRECISION,
        concavity_se DOUBLE PRECISION,
        concave_points_se DOUBLE PRECISION,
        symmetry_se DOUBLE PRECISION,
        fractal_dimension_se DOUBLE PRECISION,
        radius_worst DOUBLE PRECISION,
        texture_worst DOUBLE PRECISION,
        perimeter_worst DOUBLE PRECISION,
        area_worst DOUBLE PRECISION,
        smoothness_worst DOUBLE PRECISION,
        compactness_worst DOUBLE PRECISION,
        concavity_worst DOUBLE PRECISION,
        concave_points_worst DOUBLE PRECISION,
        symmetry_worst DOUBLE PRECISION,
        fractal_dimension_worst DOUBLE PRECISION
    );
""")

# Daten in die Tabelle einfügen
for index, row in df.iterrows():
    cur.execute("""
        INSERT INTO wisconsin.patients (diagnosis, radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """, tuple(row))

# Änderungen speichern und Verbindung schließen
conn.commit()
cur.close()
conn.close()

