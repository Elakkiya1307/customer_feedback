# ============================
# ReviewSense – Milestone 4 (Final)
# Trend Analysis + Dashboard
# ============================

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# -------- Load Data --------
@st.cache_data
def load_data():
    return pd.read_csv("Milestone2_Sentiment_Results.csv")

df = load_data()

# -------- Page Title --------
st.title("📊 ReviewSense – Customer Feedback Insight Dashboard")

# -------- Sidebar Filters --------
st.sidebar.header("Filter Options")

sentiment_filter = st.sidebar.multiselect(
    "Select Sentiment",
    options=df["sentiment"].unique(),
    default=df["sentiment"].unique()
)

filtered_df = df[df["sentiment"].isin(sentiment_filter)]

# -------- Sentiment Distribution --------
st.subheader("Sentiment Distribution")

sentiment_counts = filtered_df["sentiment"].value_counts()

fig1, ax1 = plt.subplots()
ax1.bar(sentiment_counts.index, sentiment_counts.values)
ax1.set_xlabel("Sentiment")
ax1.set_ylabel("Number of Reviews")
st.pyplot(fig1)

# -------- Confidence Score Distribution --------
st.subheader("Confidence Score Distribution")

fig2, ax2 = plt.subplots()
ax2.hist(filtered_df["confidence_score"], bins=20, color='skyblue', edgecolor='black')
ax2.set_xlabel("Confidence Score")
ax2.set_ylabel("Frequency")
st.pyplot(fig2)

# -------- Data Preview --------
st.subheader("Processed Feedback Preview")
st.dataframe(filtered_df.head(20))

# -------- Download Option --------
st.download_button(
    label="Download Processed Data",
    data=filtered_df.to_csv(index=False),
    file_name="ReviewSense_Final_Output.csv",
    mime="text/csv"
)

st.success("✅ Milestone 4 (Trend + Dashboard) Completed Successfully")
