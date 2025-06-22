# langchain_utility
Combination of several LangChain utilities like explaining a research paper
# 🧑‍🔬 AI Research Paper Explainer

**Ask questions about any scientific paper and get concise answers backed by its content.**  
Built using `LangChain`, `OpenAI`, and `Streamlit`. Perfect for students, researchers, and AI enthusiasts.

---

## 🚀 Demo

![demo](docs/demo.gif)

Try the live version → [Streamlit App Link](https://your-streamlit-link-here)

---

## 📂 Features

- 🔍 Upload any scientific PDF or give an **arXiv ID/URL**
- 🧠 Automatically parses and indexes the paper using **chunked embeddings**
- 💬 Ask natural language questions about the paper
- 📄 Get grounded answers from the paper's content using **GPT-4o + Retrieval QA**
- 📚 Supports any academic field (ML, physics, medicine, etc.)
- 🖼️ Coming soon: math extraction, figure summarization, citation graphs

---

## 🧱 Tech Stack

- `LangChain` (RetrievalQA, FAISS, OpenAIEmbeddings)
- `OpenAI` (GPT-4o or GPT-3.5)
- `FAISS` (semantic search backend)
- `Streamlit` (interactive web UI)
- `PyMuPDF` (PDF parsing)
- `arXiv` (fetching papers)

---

## 💻 How It Works

1. **Upload** a PDF or enter an arXiv link/ID.
2. **Parse & Chunk** the paper into manageable blocks.
3. **Embed** each chunk with OpenAI embeddings.
4. **Store** in FAISS vector DB.
5. Ask a question → relevant chunks retrieved → LLM answers based on content.

---

## 📦 Installation

```bash
git clone https://github.com/Poulami-Nandi/langchain_utility.git
cd langchain_utility
pip install -r requirements.txt
```

---

## 🔐 Environment Setup

Make sure your `OPENAI_API_KEY` is available either in:

### `.streamlit/secrets.toml`
```toml
OPENAI_API_KEY = "sk-..."
```

or

### `.env`
```bash
export OPENAI_API_KEY="sk-..."
```

---

## 🧪 Run Locally

```bash
streamlit run app.py
```

You’ll be able to upload PDFs or paste an arXiv URL and begin asking questions instantly.

---

## 🏗 Project Structure

```
paper-explainer/
├── app.py
├── requirements.txt
├── .streamlit/
│   └── secrets.toml
├── src/
│   ├── loader.py
│   ├── qa_chain.py
│   └── utils.py
└── sample_papers/
    └── attention_is_all_you_need.pdf
```

---

## 📈 Coming Soon

| Feature | Description |
|---------|-------------|
| 🎯 Section-wise summarization | Auto-summarize Abstract / Methods / Results |
| 🧮 LaTeX math parsing         | Render & extract equations from papers       |
| 📊 Citation graph            | Show related works and references            |
| 📸 Figure captioning         | Use OCR / object detection to describe diagrams |
| 🤖 LLM self-evaluation       | Let the LLM judge its own confidence level   |

---

## 📃 Example Papers

Start with any of these:

- [`attention_is_all_you_need.pdf`](sample_papers/attention_is_all_you_need.pdf)
- `arxiv.org/abs/1706.03762`

---

## 🌍 Deployment on Streamlit Cloud

1. Push repo to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud) and connect your GitHub
3. Select `app.py` as entry point
4. Add your API key in **Secrets** as `OPENAI_API_KEY`

App goes live in ~30 seconds 🎉

---

## 🙋 About

**Author**: [Dr. Poulami Nandi](https://www.linkedin.com/in/poulami-nandi/)  
<img src="https://github.com/Poulami-Nandi/IV_surface_analyzer/raw/main/images/own/own_image.jpg" alt="Profile" width="150"/>  
Physicist · Quant Researcher · Data Scientist  
[University of Pennsylvania](https://live-sas-physics.pantheon.sas.upenn.edu/people/poulami-nandi) | [IIT Kanpur](https://www.iitk.ac.in/) | [TU Wien](http://www.itp.tuwien.ac.at/CPT/index.htm?date=201838&cats=xbrbknmztwd)

📧 [nandi.poulami91@gmail.com](mailto:nandi.poulami91@gmail.com), [pnandi@sas.upenn.edu](mailto:pnandi@sas.upenn.edu)  
🔗 [LinkedIn](https://www.linkedin.com/in/poulami-nandi-a8a12917b/) • [GitHub](https://github.com/Poulami-Nandi) • [Google Scholar](https://scholar.google.co.in/citations?user=bOYJeAYAAAAJ&hl=en)  

---

## 📄 License

This project is open-sourced under the MIT License. See [LICENSE](LICENSE) for details.
