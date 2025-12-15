from flask import Flask, render_template, request, redirect, url_for, Response
import db
from questions import QUESTOES

app = Flask(__name__)
db.init_db()

# Mapa rápido das questões
QUESTION_MAP = {q["id"]: q for q in QUESTOES}


# ======================================================
# HOME
# ======================================================
@app.route('/')
def index():
    intro = (
        "O objetivo desse questionário é identificar a presença de barreiras e facilitadores "
        "para a adesão à farmacoterapia em condições crônicas de saúde e, com isso, nortear "
        "as intervenções dos profissionais de saúde."
    )
    return render_template("index.html", intro=intro)


# ======================================================
# DADOS DO PACIENTE
# ======================================================
@app.route('/patient', methods=['GET', 'POST'])
def patient():
    if request.method == 'POST':
        patient_id = db.save_patient(
            request.form.get("patient_name", ""),
            request.form.get("medication", ""),
            request.form.get("disease", ""),
            request.form.get("professional_name", "")
        )
        return redirect(url_for("questions", patient_id=patient_id))

    return render_template("patient.html")


# ======================================================
# QUESTIONÁRIO
# ======================================================
@app.route('/questions/<int:patient_id>', methods=['GET', 'POST'])
def questions(patient_id):
    if request.method == 'POST':
        for q in QUESTOES:
            qid = q["id"]
            alternativa = request.form.get(f"q_{qid}_alt")
            open_text = request.form.get(f"q_{qid}_open", "").strip()
            judgement = request.form.get(f"q_{qid}_judgement", "").upper().strip()

            # ------------------------------
            # Cálculo do valor
            # ------------------------------
            if q.get("open_field") and q.get("requires_judgement"):
                if judgement in q.get("facilitador_if", []):
                    valor = 1
                elif judgement in q.get("barreira_if", []):
                    valor = -1
                else:
                    valor = 0
            else:
                valor = q.get("alternativas", {}).get(alternativa, 0)

            # ------------------------------
            # Classificação
            # ------------------------------
            is_barreira = int(
                alternativa in q.get("barreira_if", []) or
                judgement in q.get("barreira_if", [])
            )
            is_facilitador = int(
                alternativa in q.get("facilitador_if", []) or
                judgement in q.get("facilitador_if", [])
            )

            # ------------------------------
            # Texto da classificação
            # ------------------------------
            classificacao_texto = ""
            mapa_classificacao = q.get("classificacao_texto", {})

            if alternativa and alternativa in mapa_classificacao:
                classificacao_texto = mapa_classificacao[alternativa]
            if judgement and judgement in mapa_classificacao:
                classificacao_texto = mapa_classificacao[judgement]

            # ------------------------------
            # Salvar resposta
            # ------------------------------
            db.save_response(
                patient_id,
                qid,
                alternativa or "",
                valor,
                open_text,
                judgement,
                is_barreira,
                is_facilitador,
                classificacao_texto
            )

        return redirect(url_for("result", patient_id=patient_id))

    return render_template(
        "questions.html",
        questoes=QUESTOES,
        patient_id=patient_id
    )


# ======================================================
# RESULTADOS
# ======================================================
@app.route('/result/<int:patient_id>')
def result(patient_id):
    stats = db.calculate_score_and_counts(patient_id)
    raw_respostas = db.get_responses_by_patient(patient_id)

    respostas = []
    barreiras = []
    facilitadores = []

    for r in raw_respostas:
        q = QUESTION_MAP.get(r["question_id"], {})

        alternativa_label = ""
        if r.get("alternativa") and q.get("labels"):
            alternativa_label = q["labels"].get(r["alternativa"], "")

        classificacao_texto = ""
        mapa_classificacao = q.get("classificacao_texto", {})

        if r.get("alternativa") in mapa_classificacao:
            classificacao_texto = mapa_classificacao[r["alternativa"]]
        elif r.get("judgement") in mapa_classificacao:
            classificacao_texto = mapa_classificacao[r["judgement"]]

        enriched = {
            "question_text": q.get("texto", ""),
            "alternativa_label": alternativa_label,
            "open_text": r.get("open_text"),
            "judgement": r.get("judgement"),
            "valor": r.get("valor"),
            "is_barreira": r.get("is_barreira"),
            "is_facilitador": r.get("is_facilitador"),
            "classificacao_texto": classificacao_texto
        }

        respostas.append(enriched)
        if r["is_barreira"]:
            barreiras.append(enriched)
        if r["is_facilitador"]:
            facilitadores.append(enriched)

    return render_template(
        "result.html",
        stats=stats,
        respostas=respostas,
        barreiras=barreiras,
        facilitadores=facilitadores
    )


# ======================================================
# ADMIN — lista pacientes e respostas
# ======================================================
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
            question_text = q.get("texto", f"Pergunta {r['question_id']}")
            alternativa_label = ""
            if r.get("alternativa") and q.get("labels"):
                alternativa_label = q["labels"].get(r["alternativa"], "")

            enriched.append({
                "question_id": r["question_id"],
                "question_text": question_text,
                "alternativa": r.get("alternativa", ""),
                "alternativa_label": alternativa_label,
                "open_text": r.get("open_text", ""),
                "judgement": r.get("judgement", ""),
                "valor": r.get("valor", 0),
                "is_barreira": r.get("is_barreira", 0),
                "is_facilitador": r.get("is_facilitador", 0),
                "classificacao_texto": r.get("classificacao_texto", "")
            })

        stats = db.calculate_score_and_counts(pid)

        dataset.append({
            "patient": p,
            "respostas": enriched,
            "stats": stats
        })

    return render_template("admin.html", dataset=dataset)


@app.route('/admin/export')
def admin_export():
    from flask import Response

    patients = db.get_all_patients()

    def generate_csv():
        header = [
            "patient_id",
            "patient_name",
            "medication",
            "disease",
            "professional_name",
            "question_id",
            "question_text",
            "alternativa",
            "alternativa_label",
            "open_text",
            "judgement",
            "valor",
            "is_barreira",
            "is_facilitador",
            "classificacao_texto"
        ]
        yield ",".join(header) + "\n"

        for p in patients:
            respostas = db.get_responses_by_patient(p["id"])
            for r in respostas:
                q = QUESTION_MAP.get(r["question_id"], {})
                question_text = q.get("texto", f"Pergunta {r['question_id']}")
                alternativa_label = ""
                if r.get("alternativa") and q.get("labels"):
                    alternativa_label = q["labels"].get(r["alternativa"], "")
                row = [
                    str(p["id"]),
                    p["patient_name"],
                    p["medication"],
                    p["disease"],
                    p["professional_name"],
                    str(r["question_id"]),
                    question_text,
                    r.get("alternativa", ""),
                    alternativa_label,
                    r.get("open_text", ""),
                    r.get("judgement", ""),
                    str(r.get("valor", 0)),
                    str(r.get("is_barreira", 0)),
                    str(r.get("is_facilitador", 0)),
                    r.get("classificacao_texto", "")
                ]
                row_safe = [f'"{c}"' if "," in c else c for c in row]
                yield ",".join(row_safe) + "\n"

    return Response(
        generate_csv(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=patients_respostas_detalhado.csv"}
    )


@app.route('/admin/export_wide')
def admin_export_wide():
    from flask import Response
    import csv
    import io

    patients = db.get_all_patients()
    question_ids = [q["id"] for q in QUESTOES]
    question_texts = [q["texto"] for q in QUESTOES]

    output = io.StringIO()
    writer = csv.writer(output)

    # Cabeçalho
    header = ["patient_id", "patient_name", "medication", "disease", "professional_name"]
    for qid, qtext in zip(question_ids, question_texts):
        header.append(f"Q{qid} Alternativa")
        header.append(f"Q{qid} Resposta")
        header.append(f"Q{qid} Valor")
        header.append(f"Q{qid} Barreira/Facilitador")
    writer.writerow(header)

    for p in patients:
        row = [
            p["id"],
            p["patient_name"],
            p["medication"],
            p["disease"],
            p["professional_name"]
        ]

        respostas = {r["question_id"]: r for r in db.get_responses_by_patient(p["id"])}
        for qid in question_ids:
            r = respostas.get(qid)
            if r:
                q = QUESTION_MAP.get(qid, {})

                # Alternativa escolhida
                alternativa = r.get("alternativa", "")

                # Texto da resposta
                if r.get("open_text"):
                    resposta_texto = r["open_text"]
                elif alternativa and q.get("labels"):
                    resposta_texto = q["labels"].get(alternativa, alternativa)
                else:
                    resposta_texto = ""

                # Valor
                valor = r.get("valor", 0)

                # Barreira ou Facilitador
                if r.get("is_barreira"):
                    bf = "Barreira"
                elif r.get("is_facilitador"):
                    bf = "Facilitador"
                else:
                    bf = ""

                row.extend([alternativa, resposta_texto, valor, bf])
            else:
                # Se não houver resposta, deixa as 4 colunas vazias
                row.extend(["", "", "", ""])
        writer.writerow(row)

    output.seek(0)
    return Response(
        output,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=patients_respostas_wide.csv"}
    )

# =====================================================================
# MAIN — iniciar servidor
# =====================================================================
if __name__ == "__main__":
    print("Executando app.py de verdade!")
    app.run(debug=True)
