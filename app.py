import streamlit as st
import pandas as pd
import plotly.express as px
import kagglehub

st.title("🚦 VisionZero - Road Risk Intelligence Dashboard")



# Download latest version
path = kagglehub.dataset_download("saurabhshahane/road-traffic-accidents")

print("Path to dataset files:", path)

# Load Dataset
df = pd.read_csv(path + "/road-traffic-accidents.csv")

# Dataset Preview
st.subheader("Dataset Preview")
st.write(df.head())

# -----------------------------
# KPI Section
# -----------------------------
st.subheader("Key Metrics")

st.write("Total Records:", len(df))
st.write("Total Vehicle Types:", df["Type_of_vehicle"].nunique())
st.write("Total Driver Age Bands:", df["Age_band_of_driver"].nunique())

# -----------------------------
# Accidents by Day of Week
# -----------------------------
st.subheader("Accidents by Day of Week")

day_count = df["Day_of_week"].value_counts().reset_index()
day_count.columns = ["Day_of_week", "Count"]

fig1 = px.bar(day_count, x="Day_of_week", y="Count")
st.plotly_chart(fig1)

# -----------------------------
# Age Band Distribution
# -----------------------------
st.subheader("Driver Age Distribution")

age_count = df["Age_band_of_driver"].value_counts().reset_index()
age_count.columns = ["Age_band_of_driver", "Count"]

fig2 = px.pie(age_count, names="Age_band_of_driver", values="Count")
st.plotly_chart(fig2)

# -----------------------------
# Gender Distribution
# -----------------------------
st.subheader("Driver Gender Distribution")

gender_count = df["Sex_of_driver"].value_counts().reset_index()
gender_count.columns = ["Sex_of_driver", "Count"]

fig3 = px.bar(gender_count, x="Sex_of_driver", y="Count")
st.plotly_chart(fig3)

# -----------------------------
# Driving Experience Analysis
# -----------------------------
st.subheader("Driving Experience Distribution")

exp_count = df["Driving_experience"].value_counts().reset_index()
exp_count.columns = ["Driving_experience", "Count"]

fig4 = px.bar(exp_count, x="Driving_experience", y="Count")
st.plotly_chart(fig4)

# -----------------------------
# Vehicle Type Analysis
# -----------------------------
st.subheader("Vehicle Type Involvement")

vehicle_count = df["Type_of_vehicle"].value_counts().reset_index()
vehicle_count.columns = ["Type_of_vehicle", "Count"]

fig5 = px.bar(vehicle_count, x="Type_of_vehicle", y="Count")
st.plotly_chart(fig5)

# -----------------------------
# Owner of Vehicle
# -----------------------------
st.subheader("Owner of Vehicle Distribution")

owner_count = df["Owner_of_vehicle"].value_counts().reset_index()
owner_count.columns = ["Owner_of_vehicle", "Count"]

fig6 = px.bar(owner_count, x="Owner_of_vehicle", y="Count")
st.plotly_chart(fig6)

