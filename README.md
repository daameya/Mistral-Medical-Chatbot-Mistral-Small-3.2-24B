# Mistral-Medical-Chatbot-Mistral-Small-3.2-24B

# How to run?
### STEPS:

Clone the repository

```bash
git clone https://github.com/daameya/Mistral-Medical-Chatbot-Mistral-Small-3.2-24B.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
python -m venv medibot
```

```bash
source medibot/scripts/activate
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


### Create a `.env` file in the root directory and add your Pinecone & openai credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


```bash
# run the following command to store embeddings to pinecone
python store_index.py
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up localhost:
```


### Techstack Used:

- Python
- LangChain
- Flask
- Mistral Small 3.2 24B
- Pinecone