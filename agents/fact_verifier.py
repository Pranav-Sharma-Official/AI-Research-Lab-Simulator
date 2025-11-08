import google.generativeai as genai

class FactVerifier:
    def __init__(self):
        self.name = "Fact Verifier"
        self.role = "Fact-Checking Agent"
        self.goal = "Verify and correct factual claims for accuracy and reliability."

    def act(self, text_with_citations: str, model):
        prompt = (
            "You are a fact-verification assistant. Cross-check factual statements and data in the following research text. "
            "If any claim seems incorrect or exaggerated, correct it or clarify with a factual explanation. "
            "Maintain integrity, avoid speculation, and ensure scientific reliability.\n\n"
            f"---\nText to Verify:\n{text_with_citations}"
        )
        response = model.generate_content(prompt)
        return response.text
