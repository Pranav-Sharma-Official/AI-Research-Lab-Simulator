import google.generativeai as genai

class CitationBuilder:
    def __init__(self):
        self.name = "Citation Builder"
        self.role = "Reference Specialist"
        self.goal = "Add realistic, relevant citations and references to enhance credibility."

    def act(self, edited_text: str, model):
        prompt = (
            "You are a research citation expert. Append relevant, realistic, and scholarly citations to the given research paper. "
            "Format them as in-text citations (Author, Year) and create a proper reference section at the end using credible placeholder names. "
            "Ensure citations are logically connected to statements. Avoid fake or unverifiable sources.\n\n"
            f"---\nPaper:\n{edited_text}"
        )
        response = model.generate_content(prompt)
        return response.text
