import streamlit as st
import numpy as np
import pickle

# Load model
with open('randomforest.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("🎓 Prediksi Potensi Dropout Mahasiswa Jaya Jaya Institute")

# Form input
with st.form("prediction_form"):
    st.header("Masukkan Data Mahasiswa")

    debtor = st.selectbox("Apakah Penunggak UKT?", [1, 0], format_func=lambda x: "Ya" if x else "Tidak")
    tuition_fees_up_to_date = st.selectbox("UKT Sudah Lunas?", [1, 0], format_func=lambda x: "Ya" if x else "Tidak")
    gender = st.selectbox("Jenis Kelamin", [0, 1], format_func=lambda x: "Perempuan" if x == 0 else "Laki-laki")
    scholarship = st.selectbox("Penerima Beasiswa?", [1, 0], format_func=lambda x: "Ya" if x else "Tidak")
    age = st.number_input("Usia Saat Pendaftaran", min_value=17, max_value=70, value=20)
    international = st.selectbox("Mahasiswa Internasional?", [1, 0], format_func=lambda x: "Ya" if x else "Tidak")

    submitted = st.form_submit_button("Prediksi")

if submitted:
    # Urutan harus sesuai saat training model
    input_data = np.array([[debtor, tuition_fees_up_to_date, gender, scholarship, age, international]])

    # Prediksi
    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)

    st.subheader("📊 Hasil Prediksi:")

    # Ambil prediksi dan probabilitas
    predicted_class = prediction[0]
    confidence = max(prediction_proba[0]) * 100

    if predicted_class == 1:
         st.error(f"⚠️ Mahasiswa diprediksi **Dropout**")
         st.markdown(f"**Tingkat Keyakinan Model:** {confidence:.2f}%")
         st.warning("💡 Rekomendasi: Segera lakukan bimbingan akademik, monitoring, atau intervensi dini.")
    else:
         st.success("✅ Mahasiswa diprediksi **Lulus**")
         st.markdown(f"**Tingkat Keyakinan Model:** {confidence:.2f}%")
         st.info("👍 Rekomendasi: Teruskan pemantauan rutin, berikan motivasi untuk mempertahankan performa.")
        
        