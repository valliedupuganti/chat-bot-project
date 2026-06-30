import os
import requests
import gradio as gr

# Read the API key from an environment variable
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY environment variable not found. "
        "Please set it before running the application."
    )

MODEL = "gemini-2.5-flash-lite"


def get_text_response(message, history):
    url = (
        f"https://generativelanguage.googleapis.com/v1/models/"
        f"{MODEL}:generateContent?key={API_KEY}"
    )

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": message
                    }
                ]
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)
        response.raise_for_status()

        result = response.json()

        return result["candidates"][0]["content"]["parts"][0]["text"]

    except requests.exceptions.RequestException as e:
        return f"Request Error: {e}"

    except KeyError:
        return "Error: Unexpected response received from Gemini API."


demo = gr.ChatInterface(
    fn=get_text_response,
    title="🤖 Gemini AI Chatbot",
    description="Ask me anything! Powered by Gemini 2.5 Flash Lite"
)

if __name__ == "__main__":
    demo.launch()
