# 🤖 AI Customer Support Chatbot

An AI-powered customer support chatbot that uses **Sentence Transformers** and **semantic similarity** to understand user queries and return the most relevant answers.

---

## 🚀 Features

* 🔍 Semantic search using Sentence Transformers
* ⚡ FastAPI backend for handling requests
* 💬 Streamlit-based interactive chat UI
* 📊 CSV-based knowledge base (FAQ style)
* 📈 Confidence score for each response
* 🧠 Real-time similarity matching

---

## 🛠️ Tech Stack

* Python
* Sentence Transformers (`all-MiniLM-L6-v2`)
* FastAPI
* Streamlit
* Scikit-learn (cosine similarity)
* Pandas

---

## 📂 Project Structure

```
AI-chatbot/
│
├── api.py          # FastAPI backend
├── app.py          # Streamlit frontend
├── model.py        # Core logic (embedding + similarity)
├── data.csv        # Dataset (FAQs)
├── README.md       # Project documentation
├── .gitignore      # Ignore unnecessary files
```

---

## ⚙️ How It Works

1. User enters a query in the chat UI
2. Query is converted into embeddings using Sentence Transformers
3. Cosine similarity is calculated with stored questions
4. Best match is selected based on highest similarity score
5. If score is below threshold → fallback response is returned

---

## ▶️ How to Run Locally

### 1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/AI-chatbot.git
cd AI-chatbot
```

---

### 2. Create virtual environment (recommended)

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

*(If requirements.txt is missing, install manually:)*

```
pip install fastapi uvicorn streamlit sentence-transformers scikit-learn pandas
```

---

### 4. Run backend (FastAPI)

```
uvicorn api:app --reload
```

👉 Open: http://127.0.0.1:8000/docs

---

### 5. Run frontend (Streamlit)

```
streamlit run app.py
```

👉 Open: http://localhost:8501

---

## 📊 Example Queries

* Where is my order?
* I forgot my password
* My payment failed
* I want a refund
* Speak with an agent

---

## ⚠️ Limitations

* Works only on predefined FAQ data
* No real-time database or API integration
* No conversational memory

---

## 🔮 Future Improvements

* Add RAG (Retrieval-Augmented Generation)
* Use LLMs like OpenAI / Llama
* Add conversation memory
* Deploy on cloud (Render / Railway / AWS)
* Improve dataset for better accuracy

---

## 👩‍💻 Author

**Diksha Sagar**

---

