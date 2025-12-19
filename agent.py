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
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("GOOGLE_API_KEY not found. Please set it in .env")
        return

    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0,
            api_key=api_key
        )
    except Exception as e:
        print("Failed to initialize LLM:", e)
        return

    try:
        agent = initialize_agent(
            tools=[search_patient, check_insurance, find_slots, book_appointment],
            llm=llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True
        )
    except Exception as e:
        print("Failed to initialize agent:", e)
        return

    print("Clinical Workflow Agent started")
    print("Type 'q' to quit safely")

    while True:
        try:
            user_input = input("\nClinician : ").strip()

            # ---- Explicit exit condition ----
            if user_input.lower() == "q":
                print("Clinical Workflow Agent stopped safely")
                break

            # ---- Ignore empty input ----
            if not user_input:
                print("Empty input ignored. Please enter a valid request.")
                continue

            # ---- Process request ----
            try:
                response = agent.run(user_input)
                print("\nSystem Output:", response)
            except Exception as tool_error:
                # Tool / LLM errors should NOT break loop
                print("Unable to process request:", tool_error)
                print("Agent is still running. Please try again.")

        except KeyboardInterrupt:
            # Ctrl + C handling
            print("\nSession interrupted by user (Ctrl+C)")
            break

        except Exception as unexpected_error:
            # Catch-all safety net
            print("Unexpected system error:", unexpected_error)
            print("Agent is still running.")

    print("Shutdown complete")


if __name__ == "__main__":
    main()
