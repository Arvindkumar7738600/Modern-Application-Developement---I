
import csv
import os
from flask import Flask, render_template, request
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")


def read_data():
    records = []

    # Check both the app.py folder and current working directory
    csv_path = os.path.join(BASE_DIR, "data.csv")

    if not os.path.exists(csv_path):
        csv_path = os.path.join(os.getcwd(), "data.csv")

    with open(csv_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)

        for row in reader:
            if len(row) >= 3:
                records.append({
                    "student_id": row[0].strip(),
                    "course_id": row[1].strip(),
                    "marks": float(row[2])
                })

    return records


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "GET":
        return render_template("index.html")

    id_type = request.form.get("ID", "").strip()
    id_value = request.form.get("id_value", "").strip()

    try:
        records = read_data()
    except (FileNotFoundError, ValueError):
        return render_template("index.html", error=True)

    if id_type == "student_id":

        student_records = [
            row for row in records
            if row["student_id"] == id_value
        ]

        if not student_records:
            return render_template("index.html", error=True)

        total_marks = sum(row["marks"] for row in student_records)

        return render_template(
            "index.html",
            student_records=student_records,
            total_marks=total_marks
        )

    elif id_type == "course_id":

        course_records = [
            row for row in records
            if row["course_id"] == id_value
        ]

        if not course_records:
            return render_template("index.html", error=True)

        marks = [row["marks"] for row in course_records]

        average_marks = sum(marks) / len(marks)
        maximum_marks = max(marks)

        os.makedirs(STATIC_DIR, exist_ok=True)

        plt.figure()
        plt.hist(marks)
        plt.xlabel("Marks")
        plt.ylabel("Frequency")
        plt.savefig(os.path.join(STATIC_DIR, "histogram.png"))
        plt.close()

        return render_template(
            "index.html",
            average_marks=average_marks,
            maximum_marks=maximum_marks,
            show_histogram=True
        )

    return render_template("index.html", error=True)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
