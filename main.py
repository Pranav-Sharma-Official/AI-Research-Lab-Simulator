import os
from dotenv import load_dotenv
import google.generativeai as genai
from agents.researcher import Researcher
from agents.reviewer import Reviewer
from agents.editor import Editor
from agents.citation_builder import CitationBuilder
from agents.fact_verifier import FactVerifier
from agents.summarizer import Summarizer
from agents.research_composer import ResearchComposer

# Load .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def main():
    topic = input("Enter your research topic: ")

    # Initialize Gemini model
    model = genai.GenerativeModel("gemini-2.5-pro")

    # Initialize agents
    researcher = Researcher()
    reviewer = Reviewer()
    editor = Editor()
    citation_builder = CitationBuilder()
    fact_verifier = FactVerifier()
    summarizer = Summarizer()
    composer = ResearchComposer()

    print("\n🧠 Researcher is drafting the initial paper...")
    draft = researcher.act(topic, model)

    print("\n🔍 Reviewer is analyzing and improving the draft...")
    reviewed = reviewer.act(draft, model)

    print("\n✍️ Editor is refining and polishing the reviewed paper...")
    edited = editor.act(reviewed, model)

    print("\n🧩 Citation Builder is adding realistic references...")
    cited = citation_builder.act(edited, model)

    print("\n🧪 Fact Verifier is checking for factual accuracy...")
    verified = fact_verifier.act(cited, model)

    print("\n🧭 Summarizer is creating a concise executive summary...")
    summary = summarizer.act(verified, model)

    print("\n📚 Research Composer is integrating everything into a final unified paper...")
    all_sections = f"""
    --- Researcher Output ---
    {draft}

    --- Reviewer Output ---
    {reviewed}

    --- Editor Output ---
    {edited}

    --- Citation Builder Output ---
    {cited}

    --- Fact Verifier Output ---
    {verified}

    --- Summarizer Output ---
    {summary}
    """
    final_paper = composer.act(all_sections, topic, model)

    # Final output
    print("\n\n✅ Research Paper Generation Complete!")
    print("\n--- EXECUTIVE SUMMARY ---\n", summary)
    print("\n--- FINAL RESEARCH PAPER ---\n", final_paper)


if __name__ == "__main__":
    main()