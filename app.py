import os
import logging
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image
import time

#uncomment the following line to enable Streamlit's secrets management
#.streamlit/secrets.toml
# Access secrets
#GEMINI_SECRET_KEY = st.secrets["secrets"]["api_key"]
#print("key:"+ GEMINI_SECRET_KEY)


#.env file for secrets management
# Load environment variables from the .env file (if present)
load_dotenv()
# Access environment variables as if they came from the actual environment
GEMINI_SECRET_KEY = os.getenv('GOOGLE_GEMINI_AI_KEY')

if GEMINI_SECRET_KEY:
    # Example usage
    print(f'SECRET_KEY: {GEMINI_SECRET_KEY}')

    # Configure Gemini API Key
    genai.configure(api_key=GEMINI_SECRET_KEY)
    print("Gemini API Key configured.")

# Set up logging    
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Logging is set up.")

st.title("Chat with Gemini Vision")

# Session state to store image & messages
if "image" not in st.session_state:
    st.session_state.image = None
if "messages" not in st.session_state:
    st.session_state.messages = []
    logger.info("Session Cleared.")


# Sidebar for instructions
st.sidebar.title("Instructions")
st.sidebar.write("1. Upload an image using the file uploader.")
st.sidebar.write("2. Enter a prompt to ask questions about the image.")
st.sidebar.write("3. Click 'Submit' to get a response from Gemini Vision.")
st.sidebar.write("4. Use 'Clear History' to reset the session.")
st.sidebar.write("5. Continue the conversation with follow-up questions.")
st.sidebar.write("7. The chat history will be displayed below.")

# Gemini Vision API Call
def chat_with_gemini(image, text):
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content([image, text])
    logger.info("Gemini Vision API called successfully.")
    # Check if the response is valid
    if not response or not hasattr(response, 'text'):
        logger.error("Invalid response from Gemini Vision API.")
        return "Error: Invalid response from Gemini Vision API."
    # Return the text content of the response
    return response.text

    
# Upload Image
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if uploaded_file:
    st.session_state.image = Image.open(uploaded_file)
    st.image(st.session_state.image, caption=uploaded_file.name, width=300 )
    logger.info("Image uploaded successfully.")
else:
    st.session_state.image = None
    logger.info("No image uploaded.")


# User Prompt
prompt = st.text_input("Enter your prompt:",key="user_input")

if st.button("Submit") and prompt:
    if uploaded_file is None:
        st.warning("Please upload an image before submitting a prompt.")
        st.toast("Upload Image", icon="🖼")
    else:
        with st.spinner("Wait for it...", show_time=True):
            time.sleep(2)
            st.toast("Be Patience!", icon="⏳")
        #st.badge("Success", icon="📝", color="blue")
        st.session_state.messages.append({"role": "user", "content": prompt})
        logger.info(f"User prompt submitted")
            
            # Get AI response
        ai_response = chat_with_gemini(st.session_state.image, prompt)
        #st.badge("Success", icon="🤖", color="green")
        st.session_state.messages.append({"role": "assistant", "content": ai_response})

        logger.info(f"AI response received")
        

st.sidebar.write("### Clear Session!")
if st.sidebar.button("Clear History"):
    st.session_state.image = None
    st.session_state.messages = []
    logger.info("Session fully cleared.")
    st.toast("Chat history cleared!", icon="🧹")
    

st.write("### Chat History")
for msg in st.session_state.messages:
    col1, col2 = st.columns([1, 1], vertical_alignment="top")  # Two equal columns

    if msg["role"] == "user":
        with col1:  # Left side for user
            st.markdown("📝 **User**")
            st.success(msg["content"])  # User's message
        with col2:
            st.write("")  # Empty column to maintain alignment

    else:  # Assistant's response
        with col1:
            st.write("")  # Empty column to maintain alignment
        with col2:  # Right side for assistant
            st.markdown("🤖 **Assistant**")
            st.info(msg["content"])  # AI response
