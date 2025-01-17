from flask import Flask, render_template, request # type: ignore

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            # Mengambil input dari form
            gpa = float(request.form['gpa'])  # Nilai GPA
            extracurricular = int(request.form['extracurricular'])  # Jumlah kegiatan ekstrakurikuler
            essay_score = float(request.form['essay_score'])  # Skor esai

            # Menghitung peluang diterima berdasarkan model sederhana
            result = calculate_admission_probability(gpa, extracurricular, essay_score)
        except ValueError:
            result = "Input tidak valid. Harap masukkan angka yang benar."

    return render_template('index.html', result=result)

def calculate_admission_probability(gpa, extracurricular, essay_score):
    """
    Fungsi sederhana untuk menghitung peluang diterima di universitas.
    Model ini menggunakan bobot berikut:
    - GPA: 50%
    - Ekstrakurikuler: 30%
    - Skor Esai: 20%
    """
    gpa_weight = 0.5
    extracurricular_weight = 0.3
    essay_weight = 0.2

    # Normalisasi nilai
    normalized_gpa = min(gpa / 4.0, 1.0)  # Asumsi GPA maksimum adalah 4.0
    normalized_extracurricular = min(extracurricular / 10.0, 1.0)  # Maksimum 10 kegiatan
    normalized_essay_score = min(essay_score / 100.0, 1.0)  # Skor maksimum 100

    # Menghitung peluang
    probability = (
        (normalized_gpa * gpa_weight) +
        (normalized_extracurricular * extracurricular_weight) +
        (normalized_essay_score * essay_weight)
    ) * 100  # Konversi ke persentase

    return f"{probability:.2f}%"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
