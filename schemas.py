from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class PatientSearchRequest(BaseModel):
    name: str = Field(..., min_length=3)

class InsuranceCheckRequest(BaseModel):
    patient_id: str
    insurance_provider: str

class AppointmentSlotRequest(BaseModel):
    specialty: str
    preferred_date: date

class AppointmentBookingRequest(BaseModel):
    patient_id: str
    doctor_id: str
    slot_time: str
