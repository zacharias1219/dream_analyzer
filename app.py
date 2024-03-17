import streamlit as st
import google.generativeai as genai
from apikey import gemini_api_key

genai.configure(api_key = gemini_api_key)

generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

st.set_page_config(page_title="Dream Analyzer")

st.image("cloud-moon-logo-design-crescent-dream-vector.jpg", width=75)

st.title("Dream Analysis")

st.subheader("Analyze your dreams")

dream_description = st.text_area("Enter your dream description")

submit_button = st.button("Analyze")

if submit_button:
    prompt_parts = [
        f"I need clearly understanding of the dreams that the user has given to you and give a emotional analysis and a mental analysis of the person. Don't give your own personal meaning of the dream just the analysis of what the condition of the person is.{dream_description}. At least 150 words for each sub heading. And also give a disclaimer at the end of the analysis.",
    ]

    response = model.generate_content(prompt_parts)
    if response:
        st.title("Here is the Analysis:")
        st.write(response.text)