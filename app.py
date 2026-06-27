# AQ.Ab8RN6JsGoIeOOGIgAAg9d0OFBXn9mAPOqJq_ypUtve6ZYX9ag

import customtkinter as ctk
from chatbot import generate_response, clear_memory
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class ChatBotUI:

    def __init__(self):

        self.root = ctk.CTk()
        self.root.title("AI Assistant")
        self.root.geometry("900x650")

        # Header
        self.header = ctk.CTkFrame(self.root, height=60)
        self.header.pack(fill="x", padx=10, pady=10)

        self.title = ctk.CTkLabel(
            self.header,
            text=" AI Assistant",
            font=("Arial", 24, "bold")
        )
        self.title.pack(pady=10)

        # Chat Area
        self.chat_box = ctk.CTkTextbox(
            self.root,
            wrap="word",
            font=("Arial", 14)
        )

        self.chat_box.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.chat_box.insert("end", "🤖 Assistant: Hello! How can I help you?\n\n")
        self.chat_box.configure(state="disabled")

        # Bottom Frame
        self.bottom = ctk.CTkFrame(self.root)
        self.bottom.pack(fill="x", padx=10, pady=10)

        self.entry = ctk.CTkEntry(
            self.bottom,
            height=40,
            placeholder_text="Type your message..."
        )

        self.entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=5
        )

        self.entry.bind("<Return>", self.send_message)

        self.send_btn = ctk.CTkButton(
            self.bottom,
            text="Send",
            command=self.send_message
        )

        self.send_btn.pack(side="left", padx=5)

        self.clear_btn = ctk.CTkButton(
            self.bottom,
            text="Clear",
            command=self.clear_chat
        )

        self.clear_btn.pack(side="left", padx=5)

    def add_message(self, sender, message):

        self.chat_box.configure(state="normal")

        self.chat_box.insert(
            "end",
            f"{sender}: {message}\n\n"
        )

        self.chat_box.see("end")

        self.chat_box.configure(state="disabled")

    def send_message(self, event=None):

        user_text = self.entry.get().strip()

        if not user_text:
            return

        self.add_message("👤 You", user_text)

        self.entry.delete(0, "end")

        threading.Thread(
            target=self.get_ai_response,
            args=(user_text,),
            daemon=True
        ).start()

    def get_ai_response(self, user_text):

        try:

            response = generate_response(user_text)

            self.root.after(
                0,
                lambda: self.add_message(
                    "🤖 Assistant",
                    response
                )
            )

        except Exception as e:

            self.root.after(
                0,
                lambda: self.add_message(
                    "⚠️ Error",
                    str(e)
                )
            )

    def clear_chat(self):

        clear_memory()

        self.chat_box.configure(state="normal")

        self.chat_box.delete("1.0", "end")

        self.chat_box.insert(
            "end",
            "🤖 Assistant: Memory cleared.\n\n"
        )

        self.chat_box.configure(state="disabled")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = ChatBotUI()
    app.run()