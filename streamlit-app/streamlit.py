import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- TITLE ---
st.title("📊 Breast Cancer Data Explorer")

# --- LOAD DATA ---
st.subheader("Step 1: Load Breast Cancer Dataset")

# Always load the same file from local path
CSV_PATH = "/Users/heinerploog/Desktop/Github/wisconsin-breast-cancer/data/data.csv"

try:
    df = pd.read_csv(CSV_PATH)

    df = df[['diagnosis', 'radius_mean', 'texture_mean', 'perimeter_mean',
       'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean',
       'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
       'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
       'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
       'fractal_dimension_se', 'radius_worst', 'texture_worst',
       'perimeter_worst', 'area_worst', 'smoothness_worst',
       'compactness_worst', 'concavity_worst', 'concave points_worst',
       'symmetry_worst', 'fractal_dimension_worst']]

    # --- Show dataframe ---
    st.subheader("Data Preview")
    st.dataframe(df.head())

    # --- Show summary ---
    st.subheader("Dataset Info")
    st.write(df.describe())

    # --- Correlation Heatmap ---
    st.subheader("📈 Correlation Heatmap")
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(), fmt=".2f", cmap="coolwarm", ax=ax)
    st.pyplot(fig)

    # --- Feature Distribution ---
    # --- Feature Selection ---
    st.subheader("📉 Feature Distribution")
    column = st.selectbox("Select a feature to visualize", df.columns)
    fig2, ax2 = plt.subplots()
    sns.histplot(df[column], kde=True, ax=ax2)
    st.pyplot(fig2)

    st.subheader("📉 Feature Distributions by Diagnosis")

    columns = ['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 
               'smoothness_mean', 'compactness_mean', 'concavity_mean', 
               'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean']

    # Set up the subplots (4 rows, 3 columns)
    fig, axes = plt.subplots(4, 3, figsize=(30, 15))

    for i in range(len(columns)):
        row = i // 3  # Determine the row in the subplot grid
        col = i % 3   # Determine the column in the subplot grid
        sns.histplot(df, x=columns[i], hue='diagnosis', ax=axes[row, col])
        axes[row, col].set_title(columns[i])  # Add feature name as title

    st.pyplot(fig)

except FileNotFoundError:
    st.error(f"Could not find file: {CSV_PATH}. Make sure it exists in the project folder.")
