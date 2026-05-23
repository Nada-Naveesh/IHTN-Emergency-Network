def get_hospital(severity: str):
    if severity == "CRITICAL":
        return "City Trauma Hospital (ICU Ready)"
    elif severity == "HIGH":
        return "Emergency Care Hospital"
    elif severity == "MODERATE":
        return "General Hospital"
    else:
        return "Primary Health Center"
