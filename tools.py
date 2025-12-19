from langchain.tools import Tool
import json

PATIENT_DB = {
    "sankar": {
        "patient_id": "CLN-SK-9081",
        "name": "Sankar",
        "dob": "2003-07-14"
    }
}

def search_patient_fn(input_str: str) -> str:
    print("search_patient tool used")

    try:
        data = json.loads(input_str)
        name = data.get("name", "").lower()
    except Exception:
        name = input_str.strip().lower()

    return json.dumps(
        PATIENT_DB.get(name, {"error": "Patient not found"})
    )

def check_insurance_fn(input_str: str) -> str:
    print("check_insurance tool used")

    try:
        data = json.loads(input_str)
        patient_id = data.get("patient_id")
    except Exception:
        patient_id = input_str.strip()

    return json.dumps({
        "patient_id": patient_id,
        "provider": "HealthSure Prime",
        "policy_id": "HS-PL-7712",
        "eligible": True
    })

def find_slots_fn(input_str: str) -> str:
    print("find_slots tool used")
    return json.dumps([
        {"doctor_id": "CARD-112", "time": "11:00 AM"},
        {"doctor_id": "CARD-209", "time": "4:30 PM"}
    ])

def book_appointment_fn(input_str: str) -> str:
    print("book_appointment tool used")

    try:
        data = json.loads(input_str)
    except Exception:
        return json.dumps({"error": "Invalid booking request"})

    return json.dumps({
        "appointment_id": "APT-SK-5564",
        "status": "CONFIRMED",
        "department": "Cardiology",
        "location": "City Care Hospital"
    })

search_patient = Tool(
    name="search_patient",
    func=search_patient_fn,
    description="Find patient details using the patient's full name."
)

check_insurance = Tool(
    name="check_insurance",
    func=check_insurance_fn,
    description="Verify whether a patient has active insurance coverage."
)

find_slots = Tool(
    name="find_slots",
    func=find_slots_fn,
    description="Retrieve available appointment slots for a medical department."
)

book_appointment = Tool(
    name="book_appointment",
    func=book_appointment_fn,
    description="Book an appointment for a patient."
)
