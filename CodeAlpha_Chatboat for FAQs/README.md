# 🤖 FAQ Chatbot

A simple **FAQ Chatbot** built with **Python**, **Streamlit**, **NLTK**, and **Scikit-learn**. The chatbot uses **Natural Language Processing (NLP)** techniques such as text preprocessing, TF-IDF vectorization, and cosine similarity to answer frequently asked questions based on a predefined knowledge base.

---

## 📌 Features

- 💬 Interactive chatbot interface built with Streamlit
- 🧠 NLP-based question preprocessing
- 🔍 TF-IDF Vectorization for text representation
- 📊 Cosine Similarity for finding the best matching question
- 📁 JSON-based FAQ database
- ⚡ Fast and lightweight
- 🚫 Returns a default response for unknown questions

---

## 📂 Project Structure

```
FAQ-Chatbot/
│── app.py                 # Streamlit application
│── chatbot.py             # Chatbot logic
│── preprocess.py          # Text preprocessing
│── faq_data.json          # FAQ dataset
│── requirements.txt       # Project dependencies
│── pydeck.json            # Streamlit configuration
│── README.md              # Project documentation
```

---

## 🛠️ Technologies Used

- Python 3.x
- Streamlit
- NLTK
- Scikit-learn
- NumPy
- JSON

---

## ⚙️ How It Works

1. The chatbot loads questions and answers from **faq_data.json**.
2. Questions are preprocessed by:
   - Converting text to lowercase
   - Tokenization
   - Removing punctuation
   - Removing stop words
   - Lemmatization
3. TF-IDF converts the processed questions into numerical vectors.
4. When a user asks a question:
   - The input is preprocessed.
   - Converted into a TF-IDF vector.
   - Compared with stored questions using cosine similarity.
5. The chatbot returns:
   - The most relevant answer if the similarity score is above the threshold.
   - `"Sorry, I don't understand."` if no suitable match is found.

---

## 📁 FAQ Dataset Format

The chatbot uses a JSON file in the following format:

```json
[
  {
    "question": "What is your name?",
    "answer": "I am an FAQ chatbot."
  },
  {
    "question": "How can I contact support?",
    "answer": "Email us at support@example.com"
  }
]
```

You can easily add more question-answer pairs by editing **faq_data.json**.

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/faq-chatbot.git
```

### 2. Navigate to the Project Folder

```bash
cd faq-chatbot
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit app with:

```bash
streamlit run app.py
```

The application will open automatically in your default web browser.

---

## 📸 Application Workflow

```
User Question
      │
      ▼
Text Preprocessing
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Cosine Similarity
      │
      ▼
Best Matching FAQ
      │
      ▼
Display Answer
```

---

## 📦 Project Dependencies

- streamlit
- nltk
- scikit-learn
- numpy

Install them using:

```bash
pip install -r requirements.txt
```

---

## 💡 Future Enhancements

- 🤖 Integrate OpenAI/Gemini API for intelligent responses
- 🎤 Voice input support
- 🔊 Text-to-speech responses
- 🌍 Multi-language support
- 🗄️ Database integration (MySQL/MongoDB)
- 📈 Chat history
- 😊 Better UI/UX
- 📱 Mobile-friendly design
- 🔍 Semantic search using Sentence Transformers

---

## 📸 Screenshot

Add a screenshot of the chatbot interface here.

```
screenshots/chatbot.png
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork this repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to your branch.
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Akash Aditya**

If you found this project useful, don't forget to ⭐ star the repository!
