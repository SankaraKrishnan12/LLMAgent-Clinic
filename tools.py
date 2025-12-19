from langchain.tools import Tool
import json

PATIENT_DB = {
    "ravi kumar": {
        "patient_id": "PAT123",
        "name": "Ravi Kumar",
        "dob": "1990-06-12"
    }
}

def search_patient_fn(input_str: str) -> str:
    print("search_patient tool used")
    data = json.loads(input_str)
    return json.dumps(PATIENT_DB.get(data["name"].lower(), {"error": "Patient not found"}))

def check_insurance_fn(input_str: str) -> str:
    print("check_insurance tool used")
    data = json.loads(input_str)
    return json.dumps({
        "patient_id": data["patient_id"],
        "eligible": True
    })

def find_slots_fn(input_str: str) -> str:
    print("find_slots tool used")
    return json.dumps([
        {"doctor_id": "DOC45", "time": "10:30 AM"},
        {"doctor_id": "DOC78", "time": "2:00 PM"}
    ])

def book_appointment_fn(input_str: str) -> str:
    print("book_appointment tool used")
    data = json.loads(input_str)
    return json.dumps({
        "appointment_id": "APT999",
        "status": "CONFIRMED"
    })

search_patient = Tool(
    name="search_patient",
    func=search_patient_fn,
    description="Find patient details using the patient's name."
)

check_insurance = Tool(
    name="check_insurance",
    func=check_insurance_fn,
    description="Check whether a patient has valid insurance."
)

find_slots = Tool(
    name="find_slots",
    func=find_slots_fn,
    description="Find available appointment slots for a medical specialty."
)

book_appointment = Tool(
    name="book_appointment",
    func=book_appointment_fn,
    description="Book an appointment for a patient."
)
