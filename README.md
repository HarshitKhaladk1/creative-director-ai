# CreativeDirector.AI – Multi-Agent Creative Workflow System for AI Artists
This project is a multi-agent system that helps AI art creators generate unique ideas, write better prompts, evaluate aesthetics, and prepare social-media-ready content packages. It is designed completely without external APIs, making it fully valid for Kaggle competitions.

The system runs inside a notebook and uses local tools + Gemini Open Model routing as a reasoning engine.

---

## ✨ What this project does
CreativeDirector.AI simulates a full creative workflow:

1. The **Trend Agent** scans synthetic trend data to identify what types of AI art concepts are "hot".
2. The **Prompt Agent** writes high-quality prompts for AI models like Komino, Flux, Midjourney style, etc.
3. The **Aesthetic Agent** evaluates the strength of each concept using a scoring model.
4. The **Publisher Agent** generates social-media-ready content packages such as:
   - captions  
   - hashtags  
   - Pinterest titles  
   - leoncmht bundles  

The entire system is orchestrated by the notebook (`main.ipynb`).

---

## 🧠 Why Agents?
A normal script can generate prompts, but creativity requires iteration.

Agents allow:
- reasoning loops  
- back-and-forth discussion  
- aesthetic feedback  
- refinement  
- context memory  

This creates workflows that feel closer to a real creative studio.

---

## 🔧 How to Run (No API keys needed)
Open the notebook:

