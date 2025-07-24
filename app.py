from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from dotenv import load_dotenv
from src.prompt import *
import os

# Flask App
app = Flask(__name__)

# Load Environment Variables
load_dotenv()
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Embeddings & Pinecone Setup
embeddings = download_hugging_face_embeddings()

index_name = "medical-chatbot"
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# Chat Model (OpenRouter)
chatModel = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENAI_API_KEY,
    model="mistralai/mistral-small-3.2-24b-instruct:free"
)

# Prompt Template with Memory
prompt = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template(
            "You are a helpful and friendly medical assistant. Use the context of the conversation to answer questions briefly and clearly."
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{question}")
    ]
)

# Conversation Memory Setup
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# LLMChain with Memory
conversation = LLMChain(
    llm=chatModel,
    prompt=prompt,
    memory=memory,
    verbose=True,
)

# Routes
@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    print("User input:", msg)

    response = conversation.invoke({"question": msg})
    print("Response:", response["text"])
    return str(response["text"])

# Run App
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
