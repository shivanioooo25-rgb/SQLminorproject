

def classify_risk(payload):

    payload = payload.upper()

    # High Risk
    if "DROP" in payload or "UNION" in payload:
        return "HIGH"

    # Medium Risk
    elif "OR" in payload or "AND" in payload:
        return "MEDIUM"

    # Low Risk
    elif "--" in payload or "#" in payload:
        return "LOW"

    # Safe Input
    else:
        return "SAFE"