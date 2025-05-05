import pandas as pd
import streamlit as st

st.set_page_config(page_title="BBtLB Lineup Generator", layout="wide")

st.title("🧠 Big Bank Take Little Bank – Fantasy Lineup Generator")

# Input: Google Sheets URL
sheet_url = st.text_input("Paste your Google Sheets link (CSV format)", "")

if sheet_url:
    if "edit#gid=" in sheet_url:
        csv_url = sheet_url.replace("edit#gid=", "export?format=csv&gid=")
    else:
        csv_url = sheet_url

    try:
        df = pd.read_csv(csv_url)

        st.subheader("📊 Player Projections")
        st.dataframe(df)

        # Simple Value Score calculation
        df["ValueScore"] = df["Projection"] / df["Salary"] * 1000
        top_players = df.sort_values("ValueScore", ascending=False).head(10)

        st.subheader("🔥 Top Value Plays")
        st.table(top_players[["Player", "Team", "Position", "Salary", "Projection", "ValueScore"]])

        st.success("✅ Data loaded and processed.")
    except Exception as e:
        st.error(f"Failed to load sheet: {e}")