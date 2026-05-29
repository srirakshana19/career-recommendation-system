import streamlit as st
import matplotlib.pyplot as plt
import requests

# =========================================
# Career Roadmaps
# =========================================

career_roadmaps = {

    "Data Scientist": [
        "Learn Python",
        "Learn Pandas & NumPy",
        "Study Machine Learning",
        "Build Projects",
        "Learn Deep Learning"
    ],

    "AI Engineer": [
        "Learn Python",
        "Learn Machine Learning",
        "Learn Deep Learning",
        "Build AI Projects",
        "Deploy Models"
    ],

    "Web Developer": [
        "Learn HTML",
        "Learn CSS",
        "Learn JavaScript",
        "Learn React",
        "Build Full Stack Projects"
    ],

    "UI/UX Designer": [
        "Learn Figma",
        "Learn UX Principles",
        "Build Design Portfolio",
        "Practice Wireframing"
    ]
}

# =========================================
# Career Skills
# =========================================

career_skills = {

    "Data Scientist": [
        "Python",
        "Machine Learning",
        "SQL",
        "Pandas"
    ],

    "AI Engineer": [
        "Python",
        "Deep Learning",
        "TensorFlow",
        "Machine Learning"
    ],

    "Web Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React"
    ],

    "UI/UX Designer": [
        "Figma",
        "Creativity",
        "Wireframing",
        "UI Design"
    ]
}

# =========================================
# Streamlit Config
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
# Inputs
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
# Recommendation Logic
# =========================================

if st.button("🚀 Recommend Career"):

    if skills and interests:

        # Temporary Local Recommendation System

        results = [
            ("Data Scientist", 95),
            ("AI Engineer", 90),
            ("Web Developer", 75),
            ("UI/UX Designer", 65)
        ]

        st.subheader("✨ Recommended Careers")

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
        # Chart
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

    else:

        st.warning("⚠️ Please enter skills and interests.")
