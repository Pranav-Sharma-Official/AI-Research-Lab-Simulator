import google.generativeai as genai

class Summarizer:
    def __init__(self):
        self.name = "Summarizer"
        self.role = "Executive Summarizer"
        self.goal = "Condense entire research into a concise, professional executive summary."

    def act(self, verified_text: str, model):
        prompt = (
            "You are a scientific summarizer. Produce a concise 200-word executive summary of the verified research paper below. "
            "Ensure it highlights the research objective, methodology, key findings, and significance. "
            "Keep it formal, cohesive, and suitable for inclusion at the start of the paper.\n\n"
            f"---\nVerified Paper:\n{verified_text}"
        )
        response = model.generate_content(prompt)
        return response.text
