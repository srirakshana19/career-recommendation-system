import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("careers.csv")

# Combine features
df["combined"] = (
    df["Skills"] + " " +
    df["Interests"] + " " +
    df["Personality"]
)

# Vectorization
vectorizer = TfidfVectorizer()

vectors = vectorizer.fit_transform(df["combined"])

# Recommendation Function
def recommend_career(skills, interests, personality):

    user_input = skills + " " + interests + " " + personality

    user_vector = vectorizer.transform([user_input])

    similarity = cosine_similarity(user_vector, vectors)

    similarity_scores = similarity[0]

    top_indexes = similarity_scores.argsort()[-3:][::-1]

    recommendations = []

    for index in top_indexes:

        career = df.iloc[index]["Career"]

        score = round(similarity_scores[index] * 100, 2)

        recommendations.append((career, score))

    return recommendations