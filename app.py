from flask import Flask, render_template, request, redirect, url_for, send_file
import db
from questions import QUESTOES
import io, csv

app = Flask(__name__)
db.init_db()

# Mapa para lookup rápido das perguntas
QUESTION_MAP = {q["id"]: q for q in QUESTOES}

@app.route('/')
def index():
    intro = (
        "O objetivo desse questionário é identificar a presença de barreiras e facilitadores "
        "para a adesão à farmacoterapia em condições crônicas de saúde. "
        "O questionário deve ser aplicado pelo profissional de saúde ao paciente."
    )
    return render_template("index.html", intro=intro)

@app.route('/patient', methods=['GET', 'POST'])
def patient():
    if request.method == 'POST':
        patient_name = request.form.get('patient_name', '')
        medication = request.form.get('medication', '')
        disease = request.form.get('disease', '')
        professional_name = request.form.get('professional_name', '')
        pid = db.save_patient(patient_name, medication, disease, professional_name)
        return redirect(url_for('questions', patient_id=pid))
    return render_template("patient.html")

@app.route('/questions/<int:patient_id>', methods=['GET', 'POST'])
def questions(patient_id):

    if request.method == 'POST':
        for q in QUESTOES:
            qid = q["id"]
            key_alt = f"q_{qid}_alt"
            key_open = f"q_{qid}_open"
            key_judgement = f"q_{qid}_judgement"

            alternativa = request.form.get(key_alt)
            open_text = request.form.get(key_open, '')
            judgement = request.form.get(key_judgement, '')

            # calcular valor
            if q.get("open_field") and q.get("requires_judgement"):
                if judgement.upper() in ("CORRETO", "ALFABETIZADO"):
                    valor = 1
                else:
                    valor = -1
            else:
                valor = q.get("alternativas", {}).get(alternativa, 0)

            # barreira/facilitador
            is_barreira = 0
            is_facilitador = 0

            if judgement.upper() in q.get("barreira_if", []):
                is_barreira = 1
            if judgement.upper() in q.get("facilitador_if", []):
                is_facilitador = 1

            if alternativa in q.get("barreira_if", []):
                is_barreira = 1
            if alternativa in q.get("facilitador_if", []):
                is_facilitador = 1

            db.save_response(
                patient_id, qid, alternativa or "", valor,
                open_text, judgement.upper(), is_barreira, is_facilitador
            )
        return redirect(url_for('result', patient_id=patient_id))

    return render_template("questions.html", questoes=QUESTOES, patient_id=patient_id)

@app.route('/result/<int:patient_id>')
def result(patient_id):
    stats = db.calculate_score_and_counts(patient_id)
    respostas = db.get_patient_responses(patient_id)
    return render_template("result.html", stats=stats, respostas=respostas)


# =====================================================================
# ADMIN — Ver todos os pacientes e todas as respostas organizadas
# =====================================================================

@app.route('/admin')
def admin():
    patients = db.get_all_patients()
    dataset = []

    for p in patients:
        pid = p["id"]
        respostas = db.get_responses_by_patient(pid)

        enriched = []
        for r in respostas:
            q = QUESTION_MAP.get(r["question_id"], {})
            pergunta = q.get("texto", f"Pergunta {r['question_id']}")
            alt_label = ""
            if r.get("alternativa") and q.get("labels"):
                alt_label = q["labels"].get(r["alternativa"], "")

            enriched.append({
                "question_id": r["question_id"],
                "question_text": pergunta,
                "alternativa": r.get("alternativa", ""),
                "alternativa_label": alt_label,
                "valor": r.get("valor"),
                "open_text": r.get("open_text"),
                "judgement": r.get("judgement"),
                "is_barreira": r.get("is_barreira"),
                "is_facilitador": r.get("is_facilitador")
            })

        stats = db.calculate_score_and_counts(pid)

        dataset.append({
            "patient": p,
            "respostas": enriched,
            "stats": stats
        })

    return render_template("admin.html", dataset=dataset)


# =====================================================================
# EXPORTAÇÃO CSV
# =====================================================================

@app.route('/admin/export')
def admin_export():
    all_responses = db.get_all_responses()

    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(["id","patient_id","question_id","question_text",
                     "alternativa","alternativa_label","valor",
                     "open_text","judgement","is_barreira","is_facilitador"])

    for r in all_responses:
        q = QUESTION_MAP.get(r["question_id"], {})
        qtext = q.get("texto", "")
        alt_label = ""
        if r.get("alternativa") and q.get("labels"):
            alt_label = q["labels"].get(r["alternativa"], "")

        writer.writerow([
            r["id"], r["patient_id"], r["question_id"], qtext,
            r.get("alternativa",""), alt_label,
            r.get("valor",""), r.get("open_text",""),
            r.get("judgement",""),
            r.get("is_barreira",""), r.get("is_facilitador","")
        ])

    buf.seek(0)
    return send_file(
        io.BytesIO(buf.getvalue().encode('utf-8')),
        download_name="bfaf_responses.csv",
        as_attachment=True,
        mimetype="text/csv"
    )


# =====================================================================
# MAIN — iniciar servidor
# =====================================================================
if __name__ == "__main__":
    print("Executando app.py de verdade!")
    app.run(debug=True)
