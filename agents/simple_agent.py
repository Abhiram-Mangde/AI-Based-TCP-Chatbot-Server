from agents.base_agent import BaseAgent
import json

class SimpleAgent(BaseAgent):
    def __init__(self):
        self.name = "PyBot"
        # Load Q&A from file
        try:
            with open('agents/qa_data.json', 'r') as f:
                self.qa_data = json.load(f)
        except Exception:
            self.qa_data = {}

    def process(self, message: str) -> str:
        msg = message.strip().lower()
        # Check Q&A file for answer
        for key, qa in self.qa_data.items():
            # Match if keyword or prompt is in the message
            if key in msg or qa.get('prompt', '').lower() in msg:
                return qa.get('answer', '')
        # Fallback to built-in answers
        if 'your name' in msg:
            return f"I am {self.name}, your Python assistant."
        elif 'help' in msg:
            return f"I can answer Python questions, explain concepts, and help you code!"
        elif 'what can you do' in msg:
            return f"I specialize in Python Q&A and programming help."
        elif any(greet in msg for greet in ['hello', 'hi', 'hey']):
            return f"Hello! I'm {self.name}. How can I assist you with Python today?"
        elif any(bye in msg for bye in ['bye', 'exit', 'goodbye', 'see you']):
            return "Goodbye! Happy coding!"
        else:
            return f"I'm {self.name}, and I can help with Python. Try asking about lists, dicts, functions, classes, or printing!"
