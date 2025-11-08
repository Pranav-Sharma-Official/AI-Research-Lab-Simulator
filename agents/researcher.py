import google.generativeai as genai

class Researcher:
    def __init__(self):
        self.name = "Researcher"
        self.role = "Scientific Researcher"
        self.goal = "Generate a detailed, structured research draft using verified and logical knowledge."

    def act(self, topic: str, model):
        prompt = (
            f"You are a professional scientific researcher specializing in academic writing. "
            f"Your objective is to generate a complete, structured research paper on the topic: '{topic}'. "
            "Follow academic writing conventions. Include sections: Abstract, Introduction, Literature Review, Methodology, Results/Discussion, and Conclusion. "
            "Ensure each section is detailed, coherent, and written in formal academic language. Avoid fictional claims or irrelevant content. "
            "Focus on verified concepts, real-world research context, and practical implications. "
            "Use citations in parentheses like (Author, Year) but do not fabricate sources."
        )
        response = model.generate_content(prompt)
        return response.text
