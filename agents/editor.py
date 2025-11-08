import google.generativeai as genai

class Editor:
    def __init__(self):
        self.name = "Editor"
        self.role = "Academic Editor"
        self.goal = "Refine and format text for clarity, coherence, and publication-level quality."

    def act(self, reviewed_text: str, model):
        prompt = (
            "You are an experienced academic editor. Refine the following research paper for grammar, syntax, and linguistic precision. "
            "Improve transitions, sentence variety, and readability while preserving meaning and tone. "
            "Ensure it reads like a polished, professional, journal-ready document.\n\n"
            f"---\nReviewed Draft:\n{reviewed_text}"
        )
        response = model.generate_content(prompt)
        return response.text
