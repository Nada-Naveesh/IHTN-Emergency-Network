def predict_severity(symptoms: str):
    s = symptoms.lower()

    if "chest pain" in s or "breathing" in s or "unconscious" in s:
        return "CRITICAL"
    elif "accident" in s or "bleeding" in s:
        return "HIGH"
    elif "fever" in s:
        return "MODERATE"
    else:
        return "LOW"
