# Chat with Gemini Vision - Streamlit App

This is a **Streamlit-based AI chat application** that enables users to upload images and interact with Google Gemini Vision AI to get responses based on the provided image and prompt.

## 🚀 Features
- Upload an image (PNG, JPG, JPEG)
- Provide a text prompt to query the image
- Get AI-generated responses from **Google Gemini Vision API**
- View chat history
- Clear session history for a new conversation
- Logging enabled for debugging

---

## 🛠️ Setup Instructions

### 1️⃣ Local Setup

#### **Clone the Repository**
```sh
# Clone the repo
git clone https://github.com/your-repo/streamlit-gemini-vision.git
cd streamlit-gemini-vision
```

#### **Create a Virtual Environment (Optional but Recommended)**
```sh
python -m venv venv  # Create a virtual environment
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate  # On Windows
```

#### **Install Dependencies**
```sh
pip install -r requirements.txt
```

#### **Set Up API Key**
Create a `.env` file in the project root and add:
```sh
GOOGLE_GEMINI_AI_KEY=your_gemini_api_key
```
Alternatively, you can use **Streamlit Secrets** by adding the API key to `.streamlit/secrets.toml`:
```toml
[secrets]
api_key = "your_gemini_api_key"
```

#### **Run the App**
```sh
streamlit run app.py
```

Access the app at: **http://localhost:8501/**

---

## 🐳 Docker Setup

### **1️⃣ Build the Docker Image**
```sh
docker build -t streamlit-gemini .
```

### **2️⃣ Run the Docker Container**
```sh
docker run -p 8501:8501 streamlit-gemini
```

Access the app at: **http://localhost:8501/**

---

## 📝 Usage Guide
1. Upload an image using the file uploader.
2. Enter a prompt to ask questions related to the image.
3. Click "Submit" to receive a response from the Gemini Vision AI.
4. View your chat history.
5. Use "Clear History" to reset the session.

---

## 📜 File Structure
```
📂 ImageGPT/
├── .streamlit/
    ├── config.toml                 #Application config file
    ├── secrets.toml                #Environment Variable config file
├── app.py                          # Main Streamlit application
├── requirements.txt                # Required Python packages
├── .env                            # API key storage (ignored in git)
├── .streamlit/secrets.toml         # Alternative API key storage
├── Dockerfile                      # Docker configuration (simple)
└── README.md                       # Project documentation
```

---

## 📌 Requirements
- Python 3.9
- Streamlit
- Google Generative AI SDK
- Pillow
- dotenv

---
