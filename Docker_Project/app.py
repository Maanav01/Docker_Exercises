# app.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import shap
import pickle
import os

# Set page config
st.set_page_config(page_title="ML Analysis App", layout="wide")

# Sidebar navigation
page = st.sidebar.selectbox("Choose a page", ["Introduction", "Dataset Loading", "Model Training", "Visualization & SHAP"])

# Cache data loading
@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    return df, iris.target_names

# Cache model training
@st.cache_resource
def train_model(X_train, y_train, n_estimators):
    model = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
    model.fit(X_train, y_train)
    return model

# Introduction Page
if page == "Introduction":
    st.title("Machine Learning Analysis Application")
    st.header("Overview")
    st.write("""
    This application demonstrates a complete ML pipeline using the Iris dataset:
    - Dataset Loading: Load and explore the Iris dataset
    - Model Training: Train a Random Forest Classifier
    - Visualization & SHAP: Visualize results and analyze feature importance using SHAP values
    
    Use the sidebar to navigate between pages.
    """)
    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=200)

# Dataset Loading Page
elif page == "Dataset Loading":
    st.title("Dataset Loading")
    
    st.header("Load Iris Dataset")
    df, target_names = load_data()
    
    st.write("Dataset Preview:")
    st.dataframe(df.head())
    
    st.write(f"Dataset Shape: {df.shape}")
    st.write(f"Features: {list(df.columns[:-1])}")
    st.write(f"Target Classes: {list(target_names)}")
    
    show_full_data = st.checkbox("Show full dataset")
    if show_full_data:
        st.dataframe(df)
    
    # Basic statistics
    st.header("Basic Statistics")
    st.write(df.describe())

# Model Training Page
elif page == "Model Training":
    st.title("Model Training")
    
    df, target_names = load_data()
    X = df.drop('target', axis=1)
    y = df['target']
    
    # Split data
    test_size = st.slider("Test set size", 0.1, 0.5, 0.2)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    
    # Model parameters
    n_estimators = st.slider("Number of trees", 10, 200, 100)
    
    # Train model
    if st.button("Train Model"):
        with st.spinner("Training model..."):
            model = train_model(X_train, y_train, n_estimators)
            
            # Save model
            with open('model.pkl', 'wb') as f:
                pickle.dump(model, f)
            
            # Make predictions
            y_pred = model.predict(X_test)
            
            # Show results
            st.header("Model Performance")
            st.write(f"Accuracy: {accuracy_score(y_test, y_pred):.3f}")
            st.write("Classification Report:")
            st.text(classification_report(y_test, y_pred, target_names=target_names))

# Visualization & SHAP Page
elif page == "Visualization & SHAP":
    st.title("Visualization & SHAP Analysis")
    
    df, target_names = load_data()
    X = df.drop('target', axis=1)
    
    # Check if model exists
    if not os.path.exists('model.pkl'):
        st.error("Please train a model first in the Model Training page")
    else:
        # Load model
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)
        
        # Feature importance plot
        st.header("Feature Importance")
        importance = pd.DataFrame({
            'feature': X.columns,
            'importance': model.feature_importances_
        }).sort_values('importance', ascending=True)
        
        fig = px.bar(importance, x='importance', y='feature', title="Feature Importance")
        st.plotly_chart(fig, use_container_width=True)
        
        # SHAP analysis
        st.header("SHAP Values Analysis")
        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(X)
        
        # SHAP summary plot
        st.subheader("SHAP Summary Plot")
        shap_fig = go.Figure()
        shap.summary_plot(shap_values, X, plot_type="bar", show=False)
        st.pyplot(bbox_inches='tight')
        
        # SHAP values for a single prediction
        st.subheader("SHAP Values for Single Prediction")
        sample_idx = st.slider("Select sample index", 0, len(X)-1, 0)
        shap_values_sample = explainer(X.iloc[[sample_idx]])
        
        # Select the class to visualize (e.g., class 0)
        class_idx = 0  # You can make this selectable if needed
        shap_values_for_class = shap_values[class_idx][sample_idx]  # SHAP values for the selected class and sample
        
        # Create a SHAP Explanation object for the selected class
        explanation = shap.Explanation(
            values=shap_values_for_class,
            base_values=explainer.expected_value[class_idx],
            data=X.iloc[sample_idx],
            feature_names=X.columns
        )
        
        # Use waterfall_plot with the Explanation object
        shap_fig = go.Figure()
        shap.waterfall_plot(explanation, show=False)
        st.pyplot(bbox_inches='tight')
