from datetime import datetime

def log_attack(payload, risk):
    """
    Save detected SQL Injection attacks to attack_logs.txt
    """

    with open("attack_logs.txt", "a") as file:
        file.write(f"{datetime.now()} | {payload} | {risk}\n")