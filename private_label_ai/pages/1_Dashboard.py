from pathlib import Path
import streamlit as st
import pandas as pd


st.title("📈 AI-Powered Private Label Growth Advisor")

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "store_adoption_scores.csv"
if not DATA_PATH.exists():
    st.error(f"Data file not found:\n{DATA_PATH}")
    st.stop()
df = pd.read_csv(DATA_PATH)

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Stores", len(df))

c2.metric(
    "Hot Opportunities",
    len(df[df["segment"] == "Hot Opportunity"])
)

c3.metric(
    "Avg Adoption %",
    round(df["adoption_probability"].mean() * 100, 2)
)

c4.metric(
    "Potential Revenue",
    f"${int(df['potential_revenue'].sum()):,}"
)

st.divider()

st.subheader("Top 20 Opportunities")

top20 = (
    df[df["target"] == 0]
    .sort_values(
        "adoption_probability",
        ascending=False
    )
    .head(20)
)

st.dataframe(
    top20[
        [
            "store_name",
            "chain_name",
            "adoption_probability",
            "potential_revenue"
        ]
    ],
    use_container_width=True
)
