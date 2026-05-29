import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("careers.csv")

# Combine text columns
df["combined"] = (
    df["Skills"] + " " +
    df["Interests"] + " " +
    df["Personality"]
)

# Convert text into vectors
vectorizer = TfidfVectorizer()

vectors = vectorizer.fit_transform(df["combined"])

# Recommendation function
def recommend_career(skills, interests, personality):

    # User input
    user_input = skills + " " + interests + " " + personality

    # Convert user input into vector
    user_vector = vectorizer.transform([user_input])

    # Similarity calculation
    similarity = cosine_similarity(user_vector, vectors)

    similarity_scores = similarity[0]

    # Top 3 matches
    top_indexes = similarity_scores.argsort()[-3:][::-1]

    recommendations = []

    for index in top_indexes:

        career = df.iloc[index]["Career"]

        score = round(similarity_scores[index] * 100, 2)

        recommendations.append((career, score))

    return recommendations