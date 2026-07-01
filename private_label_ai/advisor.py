import streamlit as st
from google import genai

# Pass the API key when creating the client.
# For local testing you can replace the placeholder with your key.
# For deployment, read it from an environment variable or Streamlit secrets.


client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)
def ask_store_advisor(
    store_name,
    probability,
    segment,
    products,
    revenue,
    question
):

    prompt = f"""
    You are a Private Label Sales Advisor for C&S Wholesale Grocers.

    Store Name:
    {store_name}

    Adoption Probability:
    {probability:.2f}%

    Segment:
    {segment}

    Potential Revenue:
    ${revenue:,.2f}

    Recommended Products:
    {products}

    User Question:
    {question}

    Explain:
    1. Why the store should be targeted
    2. What products should be pitched
    3. Expected business impact

    Keep response business friendly.
    """

    response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=prompt
    )

    return response.text
