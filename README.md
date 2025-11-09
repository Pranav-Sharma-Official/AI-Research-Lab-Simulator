# 🧠 AI Research Lab Simulator

<p align="center">
  <img src="https://img.shields.io/badge/Streamlit-Framework-red?style=flat-square&logo=streamlit" alt="Streamlit" />
  <img src="https://img.shields.io/badge/Google-Gemini%202.5%20Pro-blue?style=flat-square&logo=google" alt="Gemini" />
  <img src="https://img.shields.io/badge/Python-3.10+-yellow?style=flat-square&logo=python" alt="Python" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License" />
</p>

<p align="center"><b>"Empowering the next generation of researchers — one AI agent at a time."</b></p>

---

## 📘 Table of Contents

01. [Overview](#-overview)
02. [Features](#-features)
03. [Architecture](#-agent-architecture)
04. [Tech Stack](#-tech-stack)
05. [Installation & Setup](#-installation--setup)
06. [Running the Application](#️-running-the-application)
07. [UI Highlights](#️-ui--ux-highlights)
08. [Innovation & Impact](#-innovation--impact)
09. [Evaluation Metrics](#-evaluation-metrics)
10. [Known Issues & Fixes](#️-known-issues--fixes)
11. [Future Scope](#-future-scope)
12. [Team & Credits](#-team--contributions)
13. [License](#-license)
14. [Report](#-report)

---

## 🚀 Overview

The **AI Research Lab Simulator** is a next-generation **multi-agent Gen AI platform** powered by **Google Gemini 2.5 Pro**, designed to **autonomously generate, review, and finalize research papers**. It replicates the roles of human researchers — from ideation to publication.

View my live project here: [**PROJECT**](https://pranav-sharma-ai-research-lab-simulator.streamlit.app/)

> ⚠️ **IMPORTANT NOTE**  
> When you open the live demo link, you might see a message saying:  
> _“This app is sleeping due to inactivity.”_  
>
> ⏰ Please click the **“Wake up”** button and wait for **30–60 seconds**.  
> Streamlit Cloud will automatically restart the app — after which everything will work perfectly! 🚀  
>
> 💡 *(This is a normal behavior for free-tier hosting and doesn’t affect functionality.)*

---

## 🧩 Features

✅ Multi-Agent Workflow — 7 AI agents simulate the human research process.\
✅ Real-time Streamlit Interface with glassy, futuristic design.\
✅ Interactive AI Chat with persistent context memory.\
✅ One-click `.docx` export for editable research papers.\
✅ Secure API handling with `.env` integration.\
✅ Fully dark, modern UI optimized for laptops and tablets.

---

## 🧠 Agent Architecture

| Agent                | Role                | Description                                    |
| -------------------- | ------------------- | ---------------------------------------------- |
| 🧠 Researcher        | Content Creator     | Generates a detailed draft on the given topic. |
| 🔍 Reviewer          | Logic Analyst       | Refines structure and logical accuracy.        |
| ✍️ Editor            | Language Expert     | Polishes grammar, tone, and readability.       |
| 🧩 Citation Builder  | Reference Curator   | Adds citations and references.                 |
| 🧪 Fact Verifier     | Accuracy Specialist | Ensures factual correctness.                   |
| 🧭 Summarizer        | Synthesizer         | Produces a 200-word executive summary.         |
| 📚 Research Composer | Integrator          | Combines all outputs into one cohesive paper.  |

---

## 🏗️ Tech Stack

* **Language:** Python 3.10+
* **Framework:** Streamlit
* **Model:** Google Gemini 2.5 Pro API
* **Libraries:** `google-generativeai`, `python-docx`, `python-dotenv`, `streamlit`
* **Output Format:** `.docx`

---

## ⚙️ Installation & Setup

```bash
git clone https://github.com/Pranav-Sharma-Official/AI-Research-Lab-Simulator.git
cd AI-Research-Lab-Simulator
pip install -r requirements.txt
```

Create a `.env` file:

```bash
GEMINI_API_KEY=your_gemini_api_key_here
```

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

Steps:

1. Enter your **Gemini API Key** and **Research Topic**.
2. Click **Generate Full Research Paper**.
3. Watch each agent work in real-time.
4. Chat with your AI assistant for clarifications.
5. Export the final `.docx` research paper.

---

## 🖥️ UI & UX Highlights

<p align="center">
  <img src="assets/demo1.png" alt="UI Screenshot" width="80%"/></br>
  <img src="assets/flowchart.png" alt="Flowchart" width="80%"/>
</p>

* 🖤 Dark glassy UI with glowing cyan elements.
* 📊 Live progress tracking for all 7 agents.
* 💬 Persistent chat assistant using Streamlit’s chat UI.
* 🧾 Real-time result rendering with collapsible outputs.
* 💡 Responsive for both laptops and tablets.

---

## 💡 Innovation & Impact

This project bridges **AI and Academia**, demonstrating how Gen AI can assist in research content generation.\
It reduces manual drafting time, enhances accuracy, and supports researchers, students, and educators in academic publishing.

**Applications:**

* Thesis & Dissertation Drafting
* Automated Whitepaper Generation
* Education & Research Training
* Scientific Paper Ideation

---

## 📊 Evaluation Metrics

| Criteria      | Description                                        | Status |
| ------------- | -------------------------------------------------- | ------ |
| Functionality | 7 agents executed sequentially with distinct roles | ✅      |
| Innovation    | Multi-agent AI workflow + real-time chat           | ✅      |
| Design        | Glassmorphic UI with modern visuals                | ✅      |
| Usability     | Editable `.docx` export & persistent chat          | ✅      |
| Scalability   | Modular architecture for domain-specific research  | ✅      |

---

## ⚠️ Known Issues & Fixes

| Issue                | Description                     | Resolution                     |
| -------------------- | ------------------------------- | ------------------------------ |
| PDF Encoding         | FPDF couldn’t handle emojis     | Switched to `.docx` output     |
| Streamlit Chat Reset | Session re-runs lost chat state | Fixed via `st.session_state`   |
| API Latency          | Gemini long response time       | Added spinner + error handling |

---

## 🔮 Future Scope

* 🔗 Multi-user collaborative editing mode.
* 🎙️ Voice assistant for accessibility.
* 📡 Cloud integration (Google Drive / GitHub save).
* 🔍 Built-in plagiarism detection.
* 🧾 Auto reference verification and citation fetching.

---

## 👥 Team & Contributions

| Member            | Role                  | Contributions                                                                              |
| ----------------- | --------------------- | ------------------------------------------------------------------------------------------ |
| **Pranav Sharma** | Team Lead & Developer | Project architecture, backend, prompt engineering, Testing, documentation, and feature QA. |

---

## 🏆 Why This Project Wins

✨ End-to-end AI automation for research generation.\
✨ Functional + visually stunning interface.\
✨ Real-world applicability with Gemini 2.5 Pro.\
✨ Demonstrates deep technical and design skills.\
✨ Complete, ready-to-show hackathon-grade product.

---

## 📜 License

This project is released under the [**MIT License**](https://github.com/Pranav-Sharma-Official/AI-Research-Lab-Simulator/blob/main/LICENSE).

---

## Report

View my detailed report here: [**REPORT**](https://docs.google.com/document/d/1hRskfuVax1BKFbKbjj4qcUlu2lLuYc8f/edit?usp=sharing&ouid=116740219841548536927&rtpof=true&sd=true)

---

<p align="center">
  <img src="https://img.shields.io/badge/Developed%20with-❤️-red?style=flat-square" />
</p>

<p align="center"><b>Pranav Sharma | AI Research Lab Simulator | 2025</b></p>
