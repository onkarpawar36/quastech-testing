import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("retail_sales_dataset.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month_name()

st.title("🛒 Retail Sales Dashboard")

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"₹{df['Total Amount'].sum():,.0f}")
col2.metric("Total Orders", df.shape[0])
col3.metric("Avg Order Value", f"₹{df['Total Amount'].mean():.0f}")

# Category Sales
st.subheader("Sales by Product Category")
category_sales = df.groupby("Product Category")["Total Amount"].sum()
st.bar_chart(category_sales)

# Monthly Trend
st.subheader("Monthly Sales Trend")
monthly_sales = df.groupby("Month")["Total Amount"].sum()
st.line_chart(monthly_sales)

# Gender Distribution
st.subheader("Revenue by Gender")
gender_sales = df.groupby("Gender")["Total Amount"].sum()
st.bar_chart(gender_sales)

# Raw Data
with st.expander("View Raw Data"):
    st.dataframe(df)
