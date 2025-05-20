import streamlit as st
from PIL import Image

# ---------------------- SETTINGS ----------------------
st.set_page_config(page_title="Venkatesh | Portfolio", page_icon=":wave:", layout="wide")

# Load assets
img = Image.open("my_image.jpg")  # Ensure your image is in the same folder
with open("Resume.pdf", "rb") as file:
    resume_bytes = file.read()

# ---------------------- CUSTOM CSS ----------------------
st.markdown("""
    <style>
    .main {
        background-color: #fdfdfd;
        padding: 2rem;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #1f2937;
    }

    .title {
        color: #1d4ed8;
        font-size: 3.5rem;
        font-weight: 800;
        margin-bottom: 1rem;
        text-align: center;
    }

    .section {
        background-color: #f1f5f9;
        padding: 1.5rem;
        margin: 2rem 0;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
    }

    h2, .stSubheader {
        color: #0f172a;
        border-left: 4px solid #2563eb;
        padding-left: 10px;
    }

    a {
        color: #2563eb;
        font-weight: 600;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }

    .stDownloadButton button {
        background-color: #2563eb;
        color: white;
        font-weight: bold;
        padding: 0.6rem 1.2rem;
        border-radius: 8px;
        border: none;
        transition: background 0.3s ease;
    }

    .stDownloadButton button:hover {
        background-color: #1e40af;
    }

    video, img {
        border-radius: 8px;
        margin: 10px 0;
    }

    .contact a {
        display: block;
        margin-bottom: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------- HEADER ----------------------
st.markdown("<div class='title'>Hi, I'm Venkatesh 👋</div>", unsafe_allow_html=True)
st.write("### Data Analyst | ML Enthusiast")
st.image(img, width=200)

# ---------------------- ABOUT ----------------------
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.subheader("About Me")
st.write("""
I'm a passionate data analyst and AI enthusiast, working on real-world machine learning and AI projects 
like health prediction models, brain tumor classification, and AI-powered educational tools. 
Currently pursuing my final year of studies and interning at EliteTech Intern Company.
""")
st.markdown("</div>", unsafe_allow_html=True)

# ---------------------- SKILLS ----------------------
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.subheader("Skills")
st.markdown("""
- Python  
- Pandas, NumPy, Matplotlib  
- Scikit-learn, TensorFlow  
- SQL, Excel  
- Data Visualization  
- Communication & Problem-Solving
""")
st.markdown("</div>", unsafe_allow_html=True)

# ---------------------- RESUME ----------------------
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.subheader("Resume")
st.download_button("📄 Download Resume", resume_bytes, file_name="Resume.pdf")
st.markdown("</div>", unsafe_allow_html=True)

# ---------------------- PROJECTS ----------------------
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.subheader("Projects")

# Project 1
st.markdown("**[Car Price Prediction using Machine Learning](https://github.com/Venki01a/Car-Price-Prediction-2.git)**")
st.write("Built a predictive model using Random Forest.")
with open("Car Price Prediction.mp4", "rb") as f:
    st.video(f.read())

# Project 2
st.markdown("**[Movie Recommendation System](https://github.com/Venki01a/Movie-Recommendation-System.git)**")
st.write("Personalized movie recommendation using NLP and Streamlit.")
with open("Movie_recommendation.mp4", "rb") as f:
    st.video(f.read())

# Project 3
st.markdown("**[Customer Churn Prediction](https://github.com/Venki01a/Customer-Churn-Analysis.git)**")
st.write("Predicts customer churn based on financial parameters like Credit Score, Balance, and Salary.")
with open("Customer churn.mp4", "rb") as f:
    st.video(f.read())

st.markdown("</div>", unsafe_allow_html=True)

# ---------------------- EXPERIENCE ----------------------
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.subheader("Work Experience")
st.write("""
- **Data Analyst Intern | EliteTech Intern Company**  
  Developed dashboards, analyzed datasets, and contributed to decision-making reports.

- **Hackathon Participant | Geeks for Geeks Vultr Cloud Innovate Hackathon**  
  Developed a full-fledged AI guidance chatbot in a hackathon.
""")
st.markdown("</div>", unsafe_allow_html=True)

# ---------------------- CONTACT ----------------------
st.markdown("<div class='section contact'>", unsafe_allow_html=True)
st.subheader("Contact Me")
st.write("📧 Email: venkateshgarg11@gmail.com")
st.write("🔗 LinkedIn: [Venkatesh's Profile](https://www.linkedin.com/in/venkatesh-garg-17b822326)")
st.write("💻 GitHub: [github.com/Venki01a](https://github.com/Venki01a)")
st.markdown("</div>", unsafe_allow_html=True)

# ---------------------- END ----------------------
st.balloons()
