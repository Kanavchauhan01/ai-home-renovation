import streamlit as st
from google import genai
import os

# 🔐 API KEY (use Streamlit secrets later)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

st.set_page_config(page_title="AI Home Renovation Planner", layout="centered")

st.title("🏠 AI Home Renovation Planner")
st.write("Plan your renovation smartly using AI (FREE version)")

room = st.selectbox("Select room type", ["Kitchen", "Bedroom", "Living Room", "Bathroom"])
budget = st.number_input("Enter budget", min_value=5000, step=1000)

if st.button("Generate Renovation Plan"):
    prompt = f"""
    Create a detailed renovation plan for a {room}.
    Budget: {budget}.
    Include:
    1. Design idea
    2. Budget breakdown
    3. Timeline
    4. AI image generation prompt (text only)
    """

    with st.spinner("Generating plan..."):
        response = client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=prompt
        )

    st.success("Renovation Plan Ready ✅")
    st.write(response.text)
