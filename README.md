# 🤖 Gemini AI Chatbot using Gradio

A simple AI-powered chatbot built using **Google Gemini 2.5 Flash Lite API** and **Gradio**. This project demonstrates how to integrate Google's Gemini model with a user-friendly web interface and optionally deploy the application on Hugging Face Spaces.

---

## 📌 Features

- 💬 Interactive chatbot interface using Gradio
- 🚀 Powered by Google Gemini 2.5 Flash Lite
- 🌐 Uses REST API to communicate with Gemini
- 🖥️ Easy to run in Google Colab or locally
- ☁️ Supports deployment to Hugging Face Spaces
- 📦 Beginner-friendly project for learning Generative AI APIs

---

## 🏗️ Project Architecture

```text
                User
                  │
                  ▼
        Gradio Chat Interface
                  │
                  ▼
      get_text_response()
                  │
                  ▼
      Gemini REST API Request
                  │
                  ▼
       Gemini 2.5 Flash Lite
                  │
                  ▼
         AI Generated Response
                  │
                  ▼
       Displayed in Gradio UI
```

---

## 📂 Project Structure

```
.
├── ChatBot.ipynb          # Google Colab Notebook
├── app.py                 # Gradio application (for deployment)
├── requirements.txt       # Required dependencies
└── README.md
```

---

## ⚙️ Technologies Used

- Python 3
- Google Gemini API
- Gradio
- Requests
- Hugging Face Hub

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/<repository-name>.git

cd <repository-name>
```

Install the required packages:

```bash
pip install -r requirements.txt
```

or install manually

```bash
pip install gradio
pip install requests
pip install huggingface_hub
pip install google-genai
```

---

## 🔑 Configure Gemini API Key

Create a Gemini API Key from Google AI Studio.

Replace:

```python
API_KEY = "YOUR_API_KEY"
```

with your own API key.

> **Note:** Never commit your API key to GitHub. Store it using environment variables or secret management.

---

## ▶️ Running the Project

Launch the notebook in Google Colab or run the Gradio application locally.

If using Python:

```bash
python app.py
```

Gradio will start a local server and generate a URL similar to:

```
Running on local URL:
http://127.0.0.1:7860
```

Open the URL in your browser and start chatting.

---

## 💬 How It Works

1. User enters a prompt.
2. Gradio sends the prompt to the backend.
3. The backend sends an HTTP POST request to the Gemini API.
4. Gemini processes the prompt.
5. The generated response is returned.
6. Gradio displays the response in the chat window.

---

## 🌍 Deploying to Hugging Face Spaces

This project also includes code to upload the deployment files to Hugging Face Spaces.

Requirements:

- Hugging Face Account
- Access Token
- Repository (Space)

Login:

```python
from huggingface_hub import login

login(token="YOUR_HF_TOKEN")
```

Upload files:

```python
from huggingface_hub import HfApi

api = HfApi()

api.upload_file(...)
```

---

## 📸 Demo

Example conversation:

```
You:
What is Artificial Intelligence?

Gemini:
Artificial Intelligence (AI) refers to computer systems capable of performing tasks that typically require human intelligence...
```

---

## 🚀 Future Improvements

- Conversation memory
- Streaming responses
- Dark mode UI
- Voice input/output
- Image understanding (Gemini Vision)
- Chat history
- User authentication
- Docker support
- Environment variable support
- Better error handling

---

## ⚠️ Security Notice

This project is intended for educational purposes.

Before publishing or deploying:

- Remove hardcoded API keys
- Remove Hugging Face tokens
- Use environment variables
- Never expose secrets in public repositories

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Valli Edupuganti**

If you found this project helpful, consider giving it a ⭐ on GitHub!
