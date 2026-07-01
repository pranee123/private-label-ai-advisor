import streamlit as st
from google import genai

# Initialize Gemini client using Streamlit Secrets
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
You are a Private Label Sales Advisor.

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

1. Why this store should be targeted.
2. Which products should be pitched.
3. Expected business impact.
4. Give actionable recommendations.

Keep the response professional and business-friendly.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
