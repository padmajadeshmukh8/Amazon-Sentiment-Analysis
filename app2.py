import streamlit as st
import joblib
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Amazon Review Sentiment Analysis",
    page_icon="🛒",
    layout="wide"
)

# Load Model and Vectorizer
@st.cache_resource
def load_artifacts():
    model = joblib.load("sentiment_model.pkl")
    vectorizer = joblib.load("tfidf_vectorizer.pkl")
    return model, vectorizer

model, vectorizer = load_artifacts()

# Title
st.title("🛒 Amazon Product Review Sentiment Analysis")
st.markdown(
    """
    Analyze customer reviews and classify them as **Positive** or **Negative**
    using Machine Learning and Natural Language Processing.
    """
)

st.divider()

# Input Section
review = st.text_area(
    "Enter Amazon Review",
    placeholder="Example: This product exceeded my expectations. Highly recommended!",
    height=150
)

# Prediction
if st.button("Analyze Sentiment", use_container_width=True):

    if review.strip() == "":
        st.warning("Please enter a review.")
    else:

        review_vector = vectorizer.transform([review])

        prediction = model.predict(review_vector)[0]

        try:
            probability = model.predict_proba(review_vector)[0]
            confidence = max(probability) * 100
        except:
            confidence = None

        st.subheader("Prediction Result")

        if prediction == 1:
            st.success("😊 Positive Review")
        else:
            st.error("😞 Negative Review")

        if confidence:
            st.metric(
                label="Confidence Score",
                value=f"{confidence:.2f}%"
            )

st.divider()

# Sample Reviews
st.subheader("Try Sample Reviews")

col1, col2 = st.columns(2)

with col1:
    st.info(
        "This product is amazing. Quality is excellent and delivery was very fast."
    )

with col2:
    st.info(
        "Terrible product. Stopped working after two days and customer support was unhelpful."
    )

# Footer
st.markdown("---")
st.markdown(
    """
    **Tech Stack:** Python | NLP | TF-IDF Vectorization | Scikit-Learn | Streamlit
    """
)