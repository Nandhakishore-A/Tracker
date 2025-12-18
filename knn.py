import streamlit as st
import joblib
import numpy as np
import io

# =======================
# Page Configuration
# =======================
st.set_page_config(
    page_title="Purchase Prediction",
    page_icon="🛒",
    layout="centered"
)

# =======================
# App Header
# =======================
st.markdown(
    "<h1 style='text-align: center;'>🛒 Purchase Prediction System</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center;'>Upload trained model and predict purchase behavior</p>",
    unsafe_allow_html=True
)

st.divider()

# =======================
# Model Upload Section
# =======================
st.subheader("📂 Upload Trained Model (.pkl)")

uploaded_model = st.file_uploader(
    "Browse your trained model file",
    type=["pkl"]
)

AI_model = None

if uploaded_model is not None:
    try:
        AI_model = joblib.load(io.BytesIO(uploaded_model.read()))
        st.success("✅ Model loaded successfully!")
    except Exception as e:
        st.error(f"❌ Failed to load model: {e}")

st.divider()

# =======================
# Input Section
# =======================
st.subheader("📋 Customer Information")

age = st.slider(
    "Select Age",
    min_value=18,
    max_value=100,
    value=30
)

salary = st.slider(
    "Select Salary",
    min_value=10000,
    max_value=200000,
    step=5000,
    value=50000
)

st.divider()

# =======================
# Prediction Section
# =======================
if st.button("🔍 Predict Purchase"):
    if AI_model is None:
        st.warning("⚠️ Please upload the trained model first!")
    else:
        input_data = np.array([[age, salary]])
        prediction = AI_model.predict(input_data)

        st.subheader("📊 Prediction Result")

        if prediction[0] == 1:
            st.success("✅ PERSON WILL PURCHASE")
        else:
            st.warning("❌ PERSON WILL NOT PURCHASE")

# =======================
# Footer
# =======================
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: grey;'>KNN / ML Model | Streamlit App</p>",
    unsafe_allow_html=True
)
