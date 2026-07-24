from flask import Flask, request, render_template

from detector import detect_sql_injection
from risk_classifier import classify_risk
from logger import log_attack

from attack_counter import increment_attack, get_attack_count
from colour import get_alert_color

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    result = ""
    color = "green"

    if request.method == "POST":

        payload = request.form["payload"]

        if detect_sql_injection(payload):

            risk = classify_risk(payload)

            log_attack(payload, risk)

            increment_attack()

            color = get_alert_color(risk)

            result = f"⚠️ SQL Injection Detected! Risk Level: {risk}"

        else:

            result = "✅ Safe Input"

            color = "green"

    return render_template(
        "index.html",
        result=result,
        color=color
    )


@app.route("/dashboard")
def dashboard():

    try:
        with open("attack_logs.txt", "r") as file:
            logs = file.readlines()

    except FileNotFoundError:
        logs = []

    attack_count = get_attack_count()

    if attack_count == 0:
        risk = "SAFE"
        status = "No Attack"
        color = "green"
        alert_message = "🟢 System Secure"

    else:
        risk = "HIGH"
        status = "Attack Detected"
        color = "red"
        alert_message = "🔴 SQL Injection Attack Detected"

    return render_template(
        "dashboard.html",
        logs=logs,
        attack_count=attack_count,
        risk=risk,
        status=status,
        color=color,
        alert_message=alert_message
    )


if __name__ == "__main__":
    app.run(debug=True)