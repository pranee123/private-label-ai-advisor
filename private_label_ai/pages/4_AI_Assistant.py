from pathlib import Path
import streamlit as st
import pandas as pd

from advisor import ask_store_advisor

# -----------------------------
# Load Data
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "store_adoption_scores.csv"

if not DATA_PATH.exists():
    st.error(f"Data file not found:\n{DATA_PATH}")
    st.stop()

df = pd.read_csv(DATA_PATH)

# -----------------------------
# Page Title
# -----------------------------

st.title("🤖 Private Label AI Advisor")

# -----------------------------
# Store Selection
# -----------------------------

store_name = st.selectbox(
    "Select Store",
    sorted(df["store_name"].dropna().unique())
)

store_data = df[
    df["store_name"] == store_name
].iloc[0]

# -----------------------------
# Metrics
# -----------------------------

col1, col2, col3 = st.columns(3)

col1.metric(
    "Adoption Probability",
    f"{store_data['adoption_probability']*100:.2f}%"
)

col2.metric(
    "Segment",
    store_data["segment"]
)

col3.metric(
    "Potential Revenue",
    f"${store_data['potential_revenue']:,.0f}"
)

# -----------------------------
# Question
# -----------------------------

question = st.text_area(
    "Ask a business question",
    value="Why should I target this store?"
)

# -----------------------------
# AI Button
# -----------------------------

if st.button("Generate AI Recommendation"):

    with st.spinner("Analyzing..."):

        response = ask_store_advisor(
            store_name=store_data["store_name"],
            probability=store_data["adoption_probability"] * 100,
            segment=store_data["segment"],
            products=[
                "FROSTED FLAKES CEREAL",
                "RAISIN BRAN"
            ],
            revenue=store_data["potential_revenue"],
            question=question
        )

    st.success("Analysis Complete")

    st.markdown("### AI Recommendation")

    st.write(response)
