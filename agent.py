from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
from dotenv import load_dotenv
import os

from tools import (
    search_patient,
    check_insurance,
    find_slots,
    book_appointment
)

load_dotenv()

def main():
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0,
        api_key=os.getenv("GOOGLE_API_KEY")
    )

    agent = initialize_agent(
        tools=[search_patient, check_insurance, find_slots, book_appointment],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    print("🏥 Clinical Workflow Agent (type q to quit)")

    while True:
        user_input = input("\nClinician : ").strip()
        if user_input == "q":
            break

        response = agent.run(user_input)
        print("\nSystem Output:", response)


if __name__ == "__main__":
    main()
