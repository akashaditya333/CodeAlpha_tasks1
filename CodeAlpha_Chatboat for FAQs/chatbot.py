import json

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from preprocess import preprocess

with open("faq_data.json") as file:
    faqs = json.load(file)

questions = [faq["question"] for faq in faqs]

processed_questions = [preprocess(q) for q in questions]

vectorizer = TfidfVectorizer()

question_vectors = vectorizer.fit_transform(processed_questions)

def get_answer(user_question):

    processed = preprocess(user_question)

    user_vector = vectorizer.transform([processed])

    similarity = cosine_similarity(user_vector, question_vectors)

    index = similarity.argmax()

    score = similarity[0][index]

    if score < 0.25:
        return "Sorry, I don't understand."

    return faqs[index]["answer"]