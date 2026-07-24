# colour.py

def get_alert_color(risk):
    """
    Returns the CSS color class based on the risk level.
    """

    risk = risk.upper()

    if risk == "HIGH":
        return "red"

    elif risk == "MEDIUM":
        return "orange"

    elif risk == "LOW":
        return "yellow"

    else:
        return "green"