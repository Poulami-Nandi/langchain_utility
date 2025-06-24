# 🔍 LangChain Utility – PDF & CSV Agent

A unified Streamlit app to **ask questions** from:
- 📄 Any **PDF research paper** or arXiv article
- 📊 Any **CSV dataset**

---

## 🧠 Use Cases

- **Research Paper Explainer / ATS**: Upload a paper and ask questions — just like an AI-powered assistant or screening tool.
- **CSV Analyst**: Upload your dataset and ask any question about its contents in natural language.
- Perfect for **students, researchers, analysts, and data scientists**.

---

## 🎥 Demo

![demo](docs/demo.gif)  
**Try it live** → [Streamlit App Link](https://langchainutility-8jjzqtafi8cciy8jhqdjif.streamlit.app/)

---

## 🛠 Features

| PDF Explainer | CSV Analyst |
|---------------|-------------|
| Upload or link to arXiv paper | Upload any CSV file |
| Parses content into chunks | Uses HuggingFace LLM to query data |
| Embeds chunks & builds FAISS vector store | Converts questions to Pandas queries |
| Ask questions in plain English | Real-time insights from raw data |

---

## 🧱 Tech Stack

- `LangChain` (RetrievalQA, Agents)
- `HuggingFaceHub` (FLAN-T5)
- `FAISS` (semantic similarity)
- `PyMuPDF` (PDF parsing)
- `pandas` (data processing)
- `Streamlit` (UI)

---

## 🚦 How It Works

### PDF Mode
1. Upload a PDF or enter arXiv ID.
2. Text is extracted, chunked, and embedded using `OpenAIEmbeddings`.
3. Stored in FAISS vector index.
4. A RetrievalQA chain is created.
5. You ask: *"What are the main findings?"*
6. It retrieves relevant chunks → summarizes with LLM.

### CSV Mode
1. Upload any CSV.
2. Loaded into a Pandas DataFrame.
3. You ask: *"Which product had highest sales?"*
4. HuggingFace model + LangChain agent processes and executes code securely.
5. You get an answer with explanation.

---

## 📦 Installation

```bash
git clone https://github.com/Poulami-Nandi/langchain_utility.git
cd langchain_utility
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

### `.streamlit/secrets.toml`
```toml
HUGGINGFACEHUB_API_TOKEN = "your-huggingface-token"
```

Or you can use a `.env` file:
```bash
export HUGGINGFACEHUB_API_TOKEN="your-huggingface-token"
```

No OpenAI key needed – it's 100% free using HuggingFace.

---

## 🧪 Run Locally

```bash
streamlit run streamlit_app.py
```

You'll be able to choose between:
- 🤖 Ask your research paper
- 📊 Ask your CSV

---

## 📁 Project Structure

```
langchain_utility/
├── streamlit_app.py
├── requirements.txt
├── .streamlit/
│   └── secrets.toml
├── src/
│   ├── loader.py              # PDF/arXiv text loader
│   ├── qa_chain.py            # Builds Retrieval QA chain
│   └── csv_agent.py           # CSV agent using HF model
└── sample_papers/
    └── attention_is_all_you_need.pdf
```

---

## 💡 Example Questions

**PDF Mode**
- "What are the core contributions of this paper?"
- "Which datasets were used in experiments?"
- "Summarize the methodology."

**CSV Mode**
- "What is the average sales by region?"
- "Show the top 5 products by revenue."
- "Which year had the highest growth?"

---

## 🌍 Deployment on Streamlit Cloud

1. Push your repo to GitHub
2. Connect to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Set `streamlit_app.py` as entrypoint
4. Add `HUGGINGFACEHUB_API_TOKEN` in app secrets

---

## 🙋 About

**Author**: [Dr. Poulami Nandi](https://www.linkedin.com/in/poulami-nandi-a8a12917b/)  
<img src="https://github.com/Poulami-Nandi/IV_surface_analyzer/raw/main/images/own/own_image.jpg" alt="Profile" width="150"/>  
Physicist · Quant Researcher · Data Scientist  
[University of Pennsylvania](https://live-sas-physics.pantheon.sas.upenn.edu/people/poulami-nandi) | [IIT Kanpur](https://www.iitk.ac.in/) | [TU Wien](http://www.itp.tuwien.ac.at/CPT/index.htm?date=201838&cats=xbrbknmztwd)

📧 [nandi.poulami91@gmail.com](mailto:nandi.poulami91@gmail.com), [pnandi@sas.upenn.edu](mailto:pnandi@sas.upenn.edu)  
🔗 [LinkedIn](https://www.linkedin.com/in/poulami-nandi-a8a12917b/) • [GitHub](https://github.com/Poulami-Nandi) • [Google Scholar](https://scholar.google.co.in/citations?user=bOYJeAYAAAAJ&hl=en)  

---

## 📄 License

This project is open-sourced under the MIT License. See [LICENSE](LICENSE) for details.
