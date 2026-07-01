from pathlib import Path
import streamlit as st
import pandas as pd
from google import genai

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "store_adoption_scores.csv"
if not DATA_PATH.exists():
    st.error(f"Data file not found:\n{DATA_PATH}")
    st.stop()
df = pd.read_csv(DATA_PATH)

st.title("🤖 Private Label AI Advisor")


store_name = st.selectbox(
    "Select Store",
    sorted(df["store_name"].dropna().unique())
)

store_data = df[
    df["store_name"] == store_name
].iloc[0]

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

question = st.text_area(
    "Ask a business question",
    "Why should I target this store?"
)

if st.button("Generate AI Recommendation"):

    prompt = f"""
    Store Name: {store_data['store_name']}
    Adoption Probability: {store_data['adoption_probability']*100:.2f}%
    Segment: {store_data['segment']}
    Potential Revenue: ${store_data['potential_revenue']:,.2f}

    Question:
    {question}

    Answer as a Private Label Growth Advisor.
    """

    with st.spinner("Analyzing..."):

        response = client.models.generate_content(
            model="gemini-2.5-pro",
            contents=prompt
        )

        st.write(response.text)
