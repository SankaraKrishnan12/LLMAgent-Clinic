def search_patient(name: str):
    return {
        "patient_id": "PAT123",
        "name": name,
        "dob": "1990-06-12"
    }

def check_insurance_eligibility(patient_id: str, insurance_provider: str):
    return {
        "patient_id": patient_id,
        "provider": insurance_provider,
        "eligible": True
    }

def find_available_slots(specialty: str, preferred_date: str):
    return [
        {"doctor_id": "DOC45", "time": "10:30 AM"},
        {"doctor_id": "DOC78", "time": "2:00 PM"}
    ]

def book_appointment(patient_id: str, doctor_id: str, slot_time: str):
    return {
        "appointment_id": "APT999",
        "status": "CONFIRMED",
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "time": slot_time
    }
