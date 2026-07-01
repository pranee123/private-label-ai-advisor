from pathlib import Path
import streamlit as st
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "store_adoption_scores.csv"
if not DATA_PATH.exists():
    st.error(f"Data file not found:\n{DATA_PATH}")
    st.stop()
df = pd.read_csv(DATA_PATH)


st.title("🏪 Store Search")

store = st.selectbox(
    "Select Store",
    sorted(df["store_name"].unique())
)

selected = df[
    df["store_name"] == store
].iloc[0]

c1, c2, c3 = st.columns(3)

c1.metric(
    "Probability",
    f"{selected['adoption_probability']*100:.2f}%"
)

c2.metric(
    "Segment",
    selected["segment"]
)

c3.metric(
    "Potential Revenue",
    f"${selected['potential_revenue']:,.0f}"
)

st.divider()

st.write("### Store Details")

st.write(
    {
        "Store Number": selected["store_nbr"],
        "Chain": selected["chain_name"],
        "State": selected["store_state"],
        "Orders": selected["total_orders"],
        "Brands": selected["total_brands"],
        "Sales": selected["total_sales"]
    }
)
