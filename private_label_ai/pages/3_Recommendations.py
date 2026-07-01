from pathlib import Path
import streamlit as st
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "store_adoption_scores.csv"
if not DATA_PATH.exists():
    st.error(f"Data file not found:\n{DATA_PATH}")
    st.stop()
df = pd.read_csv(DATA_PATH)

st.title("🛒 Product Recommendations")

recommendations = pd.DataFrame(
    {
        "Product": [
            "FROSTED FLAKES CEREAL",
            "RAISIN BRAN"
        ],
        "Priority": [
            1,
            2
        ]
    }
)

st.dataframe(
    recommendations,
    use_container_width=True
)
