import pandas as pd
import datetime
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# load dataset
df = pd.read_csv("data.csv")

# load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# encode dataset
X = model.encode(df["Question"].tolist())

# logging function
def log_chat(user_input, response, score):
    with open("chat_logs.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} | User: {user_input} | Bot: {response} | Score: {score}\n")

def chat(user_input):
    user_vec = model.encode([user_input])

    similarities = cosine_similarity(user_vec, X)

    best_index = similarities.argmax()
    score = similarities[0][best_index]

    # fallback
    if score < 0.65:
        return [{
            "answer": "Sorry, I’m not sure about that. Try asking about orders, payments, or login issues.",
            "category": "Unknown",
            "score": float(score)  
        }]

    # normal response
    return [{
        "answer": df["Answer"][best_index],
        "category": df["Category"][best_index],
        "score": float(score)  
    }]