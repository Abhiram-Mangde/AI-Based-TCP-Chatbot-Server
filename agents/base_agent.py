class BaseAgent:
    """
    Base class for AI agents. Defines the interface for processing messages.
    """
    def process(self, message: str) -> str:
        raise NotImplementedError("Subclasses should implement this method.")
