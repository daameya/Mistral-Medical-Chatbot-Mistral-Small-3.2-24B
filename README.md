# Mistral-Medical-Chatbot-Mistral-Small-3.2-24B

[![Python: 3.11](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge)](https://www.python.org/)
[![License: Apache](https://img.shields.io/badge/License-Apache-yellow.svg?style=for-the-badge)](http://www.apache.org/licenses/)
[![LLM: Mistral AI](https://img.shields.io/badge/LLM-Mistral-orange.svg?style=for-the-badge)](https://mistral.ai/)
[![Vector DB: Pinecone](https://img.shields.io/badge/DataBase-Pinecone-green.svg?style=for-the-badge)](https://www.pinecone.io/)



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

Now, open the chatbot at your localhost address.

### Techstack Used:

- Python
- LangChain
- Flask
- Mistral Small 3.2 24B
- Pinecone

# Chatbot Live Link

# Chatbot Images

![buffermemory1.png](Images%2Fbuffermemory1.png)
![buffermemory2.png](Images%2Fbuffermemory2.png)
![buffermemory3.png](Images%2Fbuffermemory3.png)

# License

Mistral-Medical-Chatbot-Mistral-Small-3.2-24B is distributed by [daameya](https://github.com/daameya) under the terms of the Apache License. See the [LICENSE](LICENSE) file for more details.

# Connect with me

- [GitHub](https://github.com/daameya)
- [LinkedIn](https://www.linkedin.com/in/ameya-damle)
- [Medium](https://medium.com/@1998ameya)
- [Email](ameyadamleuk@gmail.com)
- [Instagram](https://www.instagram.com/ameya_damle)

For queries, reach out to me on my socials.