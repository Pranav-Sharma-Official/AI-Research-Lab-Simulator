import google.generativeai as genai

class ResearchComposer:
    def __init__(self):
        self.name = "Research Composer"
        self.role = "Research Integrator and Final Composer"
        self.goal = (
            "Integrate all previously generated research segments "
            "into a single, unified, and publication-ready research paper."
        )

    def act(self, all_sections: str, topic: str, model):
        """
        Takes all outputs from other agents as a single string (all_sections)
        and returns a cohesive, well-structured, full-length final research paper.
        """
        prompt = (
            f"You are a {self.role} working on the topic: '{topic}'.\n\n"
            f"Your goal: {self.goal}\n\n"
            "Below is the collection of outputs from multiple specialized agents including "
            "Researcher, Reviewer, Editor, Citation Builder, Fact Verifier, and Summarizer.\n\n"
            "Combine, synthesize, and refine them into a single, coherent, and detailed research paper.\n\n"
            "Follow this structure:\n"
            "1. Title Page (with topic, author, and abstract)\n"
            "2. Abstract (concise summary of research)\n"
            "3. Introduction (problem background and motivation)\n"
            "4. Literature Review (related work and prior research)\n"
            "5. Methodology (explain how the study could be conducted)\n"
            "6. Results and Discussion (key findings, implications, limitations)\n"
            "7. Conclusion (summarize contributions and future scope)\n"
            "8. References (use academic-style citations — don't fabricate details but format realistically)\n\n"
            "Ensure:\n"
            "- Logical flow between sections\n"
            "- Academic tone and readability\n"
            "- Factual and contextual consistency\n"
            "- Proper paragraphing and section headers\n"
            "- Remove any repetitive or contradictory statements\n\n"
            "Here are the agent outputs for reference:\n"
            "--------------------------\n"
            f"{all_sections}\n"
            "--------------------------\n\n"
            "Now produce the final, fully integrated, publication-quality research paper "
            "as a continuous formatted text ready for inclusion in a scientific journal."
        )

        response = model.generate_content(prompt)
        return response.text