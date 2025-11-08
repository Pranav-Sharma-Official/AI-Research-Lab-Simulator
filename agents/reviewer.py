import google.generativeai as genai

class Reviewer:
    def __init__(self):
        self.name = "Reviewer"
        self.role = "Peer Reviewer"
        self.goal = "Critique and refine research drafts for logical consistency, structure, and clarity."

    def act(self, draft: str, model):
        prompt = (
            "You are a senior academic peer reviewer. Your task is to carefully review the following research draft for logical flow, argument consistency, accuracy, and completeness. "
            "Identify weaknesses, redundant sections, unsupported claims, or poorly connected ideas. "
            "After listing key feedback points, provide a revised and improved version of the paper with corrections applied. "
            "Maintain the author's intent, enhance clarity, and ensure a balanced and professional academic tone.\n\n"
            f"---\nResearch Draft:\n{draft}"
        )
        response = model.generate_content(prompt)
        return response.text
