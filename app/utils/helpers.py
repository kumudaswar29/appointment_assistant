SYMPTOM_SPECIALIZATION_MAP = {
    "fever": "General Physician",
    "cold": "General Physician",
    "cough": "General Physician",

    "headache": "Neurologist",
    "migraine": "Neurologist",

    "chest pain": "Cardiologist",
    "heart pain": "Cardiologist",

    "skin rash": "Dermatologist",
    "acne": "Dermatologist",

    "stomach pain": "Gastroenterologist",
    "vomiting": "Gastroenterologist",

    "joint pain": "Orthopedic",
    "bone pain": "Orthopedic",

    "anxiety": "Psychiatrist",
    "depression": "Psychiatrist",

    # Gynecology
    "pregnancy": "Gynecology",
    "period pain": "Gynecology",
    "irregular periods": "Gynecology",
    "women problem": "Gynecology",
}


def detect_specialization(symptoms: str):
    symptoms = symptoms.lower()

    for keyword, specialization in SYMPTOM_SPECIALIZATION_MAP.items():
        if keyword in symptoms:
            return specialization

    return "General Physician"