from google import genai
from config import API_KEY, MODEL_NAME, MAX_HISTORY, SYSTEM_PROMPT

client = genai.Client(api_key=API_KEY)

chat_history = [
    {
        "role": "user",
        "content": SYSTEM_PROMPT
    }
]


def generate_response(user_input):

    global chat_history

    chat_history.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    conversation = ""

    for msg in chat_history:
        conversation += f"{msg['role']}: {msg['content']}\n"

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=conversation
    )

    bot_reply = response.text

    chat_history.append(
        {
            "role": "assistant",
            "content": bot_reply
        }
    )

    if len(chat_history) > MAX_HISTORY:
        chat_history = chat_history[-MAX_HISTORY:]

    with open("chat_log.txt", "a", encoding="utf-8") as file:
        file.write(f"User: {user_input}\n")
        file.write(f"Bot: {bot_reply}\n\n")

    return bot_reply


def clear_memory():

    global chat_history

    chat_history = [
        {
            "role": "user",
            "content": SYSTEM_PROMPT
        }
    ]