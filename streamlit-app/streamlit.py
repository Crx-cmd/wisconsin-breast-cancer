import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px  # <--- Wichtig für alle px.* Plots
from sklearn.preprocessing import LabelEncoder

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
    
    
    # --- Introduction to Data ---

    # Beschreibung
    st.markdown("""
        ### 📊 Dataset Information

        **🎯 Target Variable (y):**
        - **Diagnosis** (M = malignant, B = benign)

        **🔬 Features (X), computed for each cell nucleus:**
        - **Radius**: mean distance from center to perimeter points
        - **Texture**: standard deviation of gray-scale values
        - **Perimeter**: contour length
        - **Area**: size of the nucleus
        - **Smoothness**: local variation in radius lengths
        - **Compactness**: (perimeter² / area – 1.0)
        - **Concavity**: severity of concave portions of the contour
        - **Concave points**: number of concave portions
        - **Symmetry**: symmetry of the nucleus shape
        - **Fractal dimension**: coastline approximation – 1

        **📏 For each feature, three measurements are provided:**
        - a. Mean
        - b. Standard error
        - c. Largest/Worst value
    """)

    st.markdown("""
        ### 🧬 Feature Descriptions

        #### 🔷 Geometric Features

        **`radius_mean`, `radius_se`, `radius_worst`**  
        **`perimeter_mean`, `perimeter_se`, `perimeter_worst`**  
        **`area_mean`, `area_se`, `area_worst`**  
        **`concavity_mean`, `concavity_se`, `concavity_worst`**  
        **`concave points_mean`, `concave points_se`, `concave points_worst`**  
        
        ---
                   
        #### 🔶 Textural Features

        **`texture_mean`, `texture_se`, `texture_worst`**  
        **`smoothness_mean`, `smoothness_se`, `smoothness_worst`**  
        **`symmetry_mean`, `symmetry_se`, `symmetry_worst`**  
                
        ---

        #### 🔷 Fractal and Density-Based Features

        **`compactness_mean`, `compactness_se`, `compactness_worst`**  
        **`fractal_dimension_mean`, `fractal_dimension_se`, `fractal_dimension_worst`**  
        

        ### 📌 Summary

        #### 🟢 **Benign Tumors**  
        - Smaller, smooth, and symmetrical cells  
        - Homogeneous texture  
        - Lower complexity

        #### 🔴 **Malignant Tumors**  
        - Larger, irregular, and asymmetrical cells  
        - Rough cell boundaries  
        - More heterogeneous texture  
        - Higher fractal complexity

        ---

        Each feature offers insight into cellular changes commonly associated with cancer. Modern classifiers (e.g., machine learning models) combine these characteristics to improve diagnostic accuracy.
    """)
    

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
    
    # 1. Dictionary mit Feature-Beschreibungen
    feature_descriptions = {
        "radius_mean": "Represents the size of the nucleus. Larger nuclei may indicate malignancy.",
        "perimeter_mean": "The perimeter of the cell. A larger perimeter can indicate malignant transformation.",
        "area_mean": "Area of the nucleus. Malignant tumors often have larger areas due to uncontrolled growth.",
        "concavity_mean": "Measures how deeply the cell boundary curves inward. Malignant cells show strong concavity.",
        "concave points_mean": "Number of concave sections on the boundary. Higher numbers are linked to malignancy.",
        "texture_mean": "Variation in gray-level pixel values. Malignant tumors often show heterogeneous textures.",
        "smoothness_mean": "Indicates smoothness of cell edges. Malignant cells often have rough boundaries.",
        "symmetry_mean": "Describes symmetry of the cell shape. Benign tumors are usually more symmetrical.",
        "compactness_mean": "Compactness = (perimeter² / area - 1.0). Lower values often mean malignancy.",
        "fractal_dimension_mean": "Reflects complexity of the cell boundary. Higher values indicate malignancy.",
        # Du kannst die "_se" und "_worst" Varianten optional verknüpfen, wenn nötig
    }

    # 2. Feature auswählen
    selected_feature = st.selectbox("Feature auswählen", options=df.columns)

    # 3. Plot anzeigen
    fig_box = px.box(df, y=selected_feature, x="diagnosis", color="diagnosis",
                    title=f"{selected_feature}: Distribution by Diagnosis")
    st.plotly_chart(fig_box)

    # 4. Beschreibung anzeigen
    base_feature = selected_feature.replace("_se", "_mean").replace("_worst", "_mean")
    if base_feature in feature_descriptions:
        st.markdown(f"📝 **Description for `{selected_feature}`**:\n{feature_descriptions[base_feature]}")
    else:
        st.markdown(f"ℹ️ No description available for `{selected_feature}`.")


  
    
    # --- Show dataframe ---
    st.subheader("Data Preview")
    st.dataframe(df.head())

    mean = df[['radius_mean', 'texture_mean', 'perimeter_mean',
       'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean',
       'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean']]
    
    # --- Show summary ---
    st.subheader("Dataset Info")
    st.write(mean.describe())

    # --- Correlation Heatmap ---

    st.subheader("📈 Correlation Heatmap")
    fig, ax = plt.subplots()
    sns.heatmap(mean.corr(), fmt=".2f", cmap="coolwarm", ax=ax)
    st.pyplot(fig)

    # --- Feature Distribution ---
    # --- Feature Selection ---
    st.subheader("📉 Feature Distribution")
    column = st.selectbox("Select a feature to visualize", df.columns)
    fig2, ax2 = plt.subplots()
    sns.histplot(df[column], kde=True, ax=ax2)
    st.pyplot(fig2)



except FileNotFoundError:
    st.error(f"Could not find file: {CSV_PATH}. Make sure it exists in the project folder.")
