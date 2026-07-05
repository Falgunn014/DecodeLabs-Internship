Custom AI Chatbot with Memory

This project was developed as part of the DecodeLabs Generative AI Internship (Week 1).

The objective of this project is to build a conversational AI chatbot that can interact with users using Google's Gemini AI model. Unlike a basic chatbot, this application maintains conversation history during the session, allowing it to generate more relevant and context-aware responses.

Project Features

- Interactive command-line chatbot
- Conversation memory
- Context-aware responses
- Powered by Google Gemini API
- Simple and easy-to-use interface
- Error handling for API requests

Technologies Used

- Python 3.12
- Google Gemini API
- google-genai
- dotenv

Project Structure

```
Task 1 - Custom AI Chatbot with Memory

app.py
chatbot.py
config.py
requirements.txt
README.md
```

Installation

Clone the repository.

```bash
git clone https://github.com/Falgunn014/DecodeLabs-Internship.git
```

Go to the project folder.

```bash
cd "Task 1 - Custom AI Chatbot with Memory"
```

Install the required packages.

```bash
pip install -r requirements.txt
```

Configuration

Open the `config.py` file and add your Gemini API key.

```python
API_KEY = "YOUR_GEMINI_API_KEY"
```

Run the Project

```bash
python app.py
```

Learning Outcomes

This project helped me understand API integration, prompt-based conversations, session memory, and building a basic AI chatbot using Python.

Author

Falgun Nagpure

DecodeLabs Generative AI Internship – Week 1
