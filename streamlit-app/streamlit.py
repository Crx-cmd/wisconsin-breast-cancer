import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- TITLE ---
st.title("📊 Breast Cancer Data Explorer")

# --- LOAD DATA ---
st.subheader("Step 1: Load CSV File")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    # --- Show dataframe ---
    st.subheader("Data Preview")
    st.dataframe(df.head())

    # --- Show summary ---
    st.subheader("Dataset Info")
    st.write(df.describe())

    # --- Correlation Heatmap ---
    st.subheader("📈 Correlation Heatmap")
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(numeric_only=True), annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    st.pyplot(fig)

    # --- Feature Selection ---
    st.subheader("📉 Feature Distribution")
    column = st.selectbox("Select a feature to visualize", df.columns)
    fig2, ax2 = plt.subplots()
    sns.histplot(df[column], kde=True, ax=ax2)
    st.pyplot(fig2)