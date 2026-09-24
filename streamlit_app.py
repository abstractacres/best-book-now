# Author: Christian M.
# Date: 2024-06-26
# Description:Streamlit app for filtering and displaying books based on user preferences

import pandas as pd
import streamlit as st

# Set page title and layout
st.set_page_config(page_title="Best Book Now", layout="wide")
st.title("🌟📚⏳ Tool for choosing what to read expeditiously.")

# Load book dataset
df = pd.read_csv("books-sep26.csv")

# Sidebar Filters
st.sidebar.header("Filter Options")

# Time Constraint Filter
max_time = st.sidebar.slider(
    "Max Time Available (Hours)",
    min_value=1,
    max_value=int(df["Time Required"].max()),
    value=int(df["Time Required"].max()),
)

# Multi-select Filters
selected_engagement = st.sidebar.multiselect(
    "Engagement Type",
    options=df["Engagement Type"].unique(),
    default=df["Engagement Type"].unique(),
)
selected_medium = st.sidebar.multiselect(
    "Medium",
    options=df["Medium"].unique(),
    default=df["Medium"].unique(),
)

selected_challenge = st.sidebar.multiselect(
    "Challenge",
    options=df["Challenge"].unique(),
    default=df["Challenge"].unique(),
)

selected_env = st.sidebar.multiselect(
    "Environment",
    options=df["Environment"].unique(),
    default=df["Environment"].unique(),
)
selected_priority = st.sidebar.multiselect(
    "Priority",
    options=df["Priority"].unique(),
    default=df["Priority"].unique(),
)

selected_goal = st.sidebar.multiselect(
    "Goal", options=df["Goal"].unique(), default=df["Goal"].unique()
)

# Apply Filtering Logic
filtered_df = df[
    (df["Time Required"] <= max_time)
    & (df["Medium"].isin(selected_medium))
    & (df["Engagement Type"].isin(selected_engagement))
    & (df["Challenge"].isin(selected_challenge))
    & (df["Environment"].isin(selected_env))
    & (df["Priority"].isin(selected_priority))
    & (df["Goal"].isin(selected_goal))
]

# Display Results
st.subheader(f"Matching Books ({len(filtered_df)})")

if not filtered_df.empty:
    for _, row in filtered_df.iterrows():
        with st.expander(f"📖 {row['Title']} by {row['Author']}"):
            st.write(f"**Medium:** {row['Medium']}")
            st.write(f"**Engagement:** {row['Engagement Type']}")
            st.write(f"**Time Required:** ~{row['Time Required']} hours")
            st.write(f"**Challenge:** {row['Challenge']}")
            st.write(f"**Environment:** {row['Environment']}")
            st.write(f"**Priority:** {row['Priority']}")
            st.write(f"**Goal:** {row['Goal']}")
else:
    st.info("No books match your current filter criteria. Try broadening your selection.")
