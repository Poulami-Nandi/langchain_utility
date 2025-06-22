# langchain_utility
Combination of several LangChain utilities like explaining a research paper
# 🧑‍🔬 AI Research Paper Explainer

Ask questions about any scientific paper and get concise answers backed by its content.  
Built with **Streamlit + LangChain + GPT-4o**.

## Demo
![demo-gif](docs/demo.gif)

## Quick Start
```bash
git clone https://github.com/<your_handle>/paper-explainer
cd paper-explainer
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...
streamlit run app.py
```
## 6 . Stretch features to add later

| Feature | Lift | Notes |
|---------|------|-------|
| Section-level summaries (“Abstract / Methods / Results”) | ⭐ | Detect headings with regex & run `map_reduce` chain |
| Math-aware parsing (LaTeX) | ⭐⭐ | Use [ScienceParse] or MathPix OCR |
| Citation graph & related-papers | ⭐⭐ | arXiv API + NetworkX + PyVis |
| Diagram extraction | ⭐⭐ | Deploy `detectron2` to isolate figures |
| Fine-tuned local model | ⭐⭐⭐ | e.g., Mistral-7B-Instruct with GGUF + `llama-cpp-python` |

---

## 7 . Deployment pointers

1. **GitHub repo** → push.  
2. **Streamlit Cloud** → *“New app ➜ pick repo ➜ main branch ➜ `app.py`”*.  
3. Add `OPENAI_API_KEY` to the web secrets panel.  
4. ⏱️ 30–60 seconds later your public demo URL is live.  

---

### Ready-made commit

1. Copy the tree above.  
2. `git init && git add . && git commit -m "✨ initial commit – paper explainer"`  
3. Push to GitHub.  
4. Share the Streamlit link on your résumé / LinkedIn.

---

**Need help customizing (e.g., adding multimodal generation)?**  
Just ping me and I’ll walk you through the tweaks! Happy hacking 🚀


