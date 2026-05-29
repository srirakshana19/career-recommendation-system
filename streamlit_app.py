import streamlit as st
import matplotlib.pyplot as plt
import requests

from backend.roadmap_engine import career_roadmaps
from backend.skill_gap_engine import career_skills

# =========================================
# Page Configuration
# =========================================

st.set_page_config(
    page_title="AI Career Recommendation System",
    page_icon="🎯",
    layout="centered"
)

# =========================================
# Custom CSS
# =========================================

st.markdown("""
<style>

.main {
    background-color: #F5F0FF;
}

h1 {
    color: #6C63FF;
    text-align: center;
    font-size: 42px;
}

.stButton > button {
    background-color: #6C63FF;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
    border: none;
}

.stButton > button:hover {
    background-color: #574bdb;
    color: white;
}

.result-card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    margin-top: 15px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    color: #333333;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# Title
# =========================================

st.title("🎯 AI Career Recommendation System")

st.write(
    "Find the best career path based on your skills, interests, and personality."
)

# =========================================
# User Inputs
# =========================================

skills = st.text_input(
    "💻 Enter Your Skills",
    placeholder="Python, SQL, Communication"
)

interests = st.text_input(
    "❤️ Enter Your Interests",
    placeholder="AI, Analytics, Design"
)

personality = st.selectbox(
    "🧠 Select Personality Type",
    ["Introvert", "Extrovert", "Ambivert"]
)

# =========================================
# Recommendation Button
# =========================================

if st.button("🚀 Recommend Career"):

    if skills and interests:

        try:

            # Send request to backend API
            response = requests.post(
                "http://127.0.0.1:8000/recommend",
                json={
                    "skills": skills,
                    "interests": interests,
                    "personality": personality
                }
            )

            # Convert response to JSON
            data = response.json()

            # Extract recommendations
            results = data["recommendations"]

            st.subheader("✨ Recommended Careers")

            # =========================================
            # Show Recommendations
            # =========================================

            for career, score in results:

                st.markdown(f"""
                <div class="result-card">

                <h3>🎓 {career}</h3>

                <p>📊 Match Score: <b>{score}%</b></p>

                </div>
                """, unsafe_allow_html=True)

                # =========================================
                # Roadmap
                # =========================================

                roadmap = career_roadmaps.get(career, [])

                if roadmap:

                    st.markdown("#### 🛣 Career Roadmap")

                    for step in roadmap:
                        st.write(f"✅ {step}")

                # =========================================
                # Skill Gap Analysis
                # =========================================

                st.markdown("#### 📈 Skill Gap Analysis")

                required_skills = career_skills.get(career, [])

                user_skills = [
                    skill.strip().lower()
                    for skill in skills.split(",")
                ]

                missing_skills = []

                for skill in required_skills:

                    if skill.lower() not in user_skills:
                        missing_skills.append(skill)

                if missing_skills:

                    st.write("🔍 Missing Skills:")

                    for skill in missing_skills:
                        st.write(f"❌ {skill}")

                else:
                    st.success("✅ You already match most required skills!")

            # =========================================
            # Career Match Chart
            # =========================================

            st.subheader("📊 Career Match Analysis")

            careers = [
                career
                for career, score in results
            ]

            scores = [
                score
                for career, score in results
            ]

            fig, ax = plt.subplots()

            ax.bar(careers, scores)

            ax.set_ylabel("Match Percentage")

            ax.set_title("Career Match Analysis")

            st.pyplot(fig)

        except:

            st.error("⚠️ Backend server is not running.")

    else:

        st.warning("⚠️ Please enter skills and interests.")

# =========================================
# Recommendation History
# =========================================

st.subheader("📜 Recommendation History")

try:

    history_response = requests.get(
        "http://127.0.0.1:8000/history"
    )

    history_data = history_response.json()

    history = history_data["history"]

    if history:

        for row in history:

            st.markdown(f"""
            <div class="result-card">

            <h4>🧠 Personality: {row[3]}</h4>

            <p><b>💻 Skills:</b> {row[1]}</p>

            <p><b>❤️ Interests:</b> {row[2]}</p>

            <p><b>🎯 Recommended Careers:</b> {row[4]}</p>

            </div>
            """, unsafe_allow_html=True)

    else:

        st.info("No recommendation history found.")

except:

    st.error("⚠️ Backend server is not running.")