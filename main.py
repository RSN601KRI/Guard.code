import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="Threat Intelligence Report Generator",
    page_icon=":shield:",  # Favicon emoji representing security
    layout="wide",  # Page layout option (wide layout)
)

# Retrieve the API key from environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Function to translate roles for Streamlit chat message
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Sidebar content
with st.sidebar:
    st.title("⚙️ Project Theme")
    st.markdown("""
    **Cybersecurity Threat Intelligence Report Generator** is an AI-powered tool that allows users to generate comprehensive, formal threat intelligence reports based on cybersecurity incidents. The AI model uses advanced natural language processing (NLP) to generate structured reports that can be used for documentation, analysis, and decision-making.

    --- 
    ### Key Features:
    - **Automated Report Generation**: Automatically generates formal reports based on user input.
    - **Detailed Cybersecurity Analysis**: Provides insights into attack types, vulnerabilities, and mitigation strategies.
    - **Formal Structure**: The report is divided into sections like Abstract, Incident Overview, Analysis, Recommendations, and Conclusion.
    - **Real-time Interaction**: Users can input event details in real-time and receive immediate report generation.

    --- 
    ### How to Use:
    1. Provide the details of the cybersecurity event in the text box.
    2. Click **Generate Report** to receive a structured threat intelligence report based on the input.
    """)

# Display the chatbot's title on the page
st.title("💻 Cybersecurity Threat Intelligence Report Generator")

# Instruction for the user
st.markdown(
    """
    **Instructions:**
    1. Please provide detailed information about the cybersecurity event you wish to generate a report for.
    2. The model will then generate a formal, structured report summarizing the attack, its impact, and defense measures.
    """
)

# Collect user input for cybersecurity event details
event_data = st.text_area(
    "Enter Cybersecurity Event Details:",
    height=150,
    placeholder="Describe the attack details, including attack type, source, impact, defenses, and mitigation steps..."
)

# Button to trigger report generation
if st.button("Generate Report"):
    if event_data:
        # Send the event data to Gemini-Pro for processing
        prompt = f"""
        Generate a formal cybersecurity threat intelligence report based on the following event:

        Event Details: {event_data}

        The report should include:
        1. **Abstract**: A concise summary of the event.
        2. **Introduction**: Context of the attack, when, where, and how it occurred.
        3. **Incident Overview**: Information on the attack's source, type, and impact.
        4. **Analysis**: Detailed analysis of the attack's methodology, vulnerabilities, and defenses.
        5. **Recommendations**: Suggested steps for prevention, mitigation, and future defense.
        6. **Conclusion**: Summary of key takeaways from the event and lessons learned.
        """

        # Add user event details into chat
        st.chat_message("user").markdown(event_data)

        # Generate the response by sending the prompt to Gemini-Pro
        gemini_response = st.session_state.chat_session.send_message(prompt)

        # Display the generated report from Gemini-Pro
        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)
    else:
        st.warning("Please enter the event details to generate the report.")
