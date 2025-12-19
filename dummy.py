from langchain.agents import initialize_agent, AgentType
from langchain.llms.fake import FakeListLLM
from tools import (
    search_patient_tool,
    insurance_check_tool,
    slot_finder_tool,
    appointment_booking_tool
)
import result_store
import json

llm = FakeListLLM(
    responses=[
        "Thought: I should find the patient\n"
        "Action: search_patient\n"
        "Action Input: Ravi Kumar",

        "Thought: I should check insurance eligibility\n"
        "Action: check_insurance\n"
        "Action Input: {\"patient_id\": \"PAT123\"}",

        "Thought: I should find available cardiology slots\n"
        "Action: find_slots\n"
        "Action Input: {\"specialty\": \"cardiology\", \"preferred_date\": \"2025-01-10\"}",

        "Thought: I should book the appointment\n"
        "Action: book_appointment\n"
        "Action Input: {\"patient_id\": \"PAT123\", \"doctor_id\": \"DOC45\", \"slot_time\": \"10:30 AM\"}",

        "Final Answer: Appointment booked successfully"
    ]
)

agent = initialize_agent(
    tools=[
        search_patient_tool,
        insurance_check_tool,
        slot_finder_tool,
        appointment_booking_tool
    ],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def run_agent(user_input: str):
    return agent.run(user_input)

if __name__ == "__main__":
    query = (
        "Schedule a cardiology follow-up for patient Ravi Kumar "
        "next week and check insurance eligibility"
    )

    agent.run(query)

    fhir_like_response = {
        "resourceType": "Appointment",
        "id": result_store.FINAL_RESULT["appointment_id"],
        "status": result_store.FINAL_RESULT["status"],
        "participant": [
            {
                "actor": {
                    "reference": f"Patient/{result_store.FINAL_RESULT['patient_id']}"
                }
            },
            {
                "actor": {
                    "reference": f"Practitioner/{result_store.FINAL_RESULT['doctor_id']}"
                }
            }
        ],
        "start": result_store.FINAL_RESULT["time"]
    }

    print(json.dumps(fhir_like_response, indent=2))
