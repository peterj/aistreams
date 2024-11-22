from dotenv import load_dotenv
from openai import AsyncOpenAI
import os
import chainlit as cl
import json

from prompts import SYSTEM_PROMPT
from tools import TOOLS

cl.instrument_openai()
load_dotenv()


client = AsyncOpenAI(api_key=os.getenv('OPENAI_API_KEY'))
settings = {
    "model": "gpt-3.5-turbo-1106",
    "temperature": 0.2,
}


@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("message_history", [
        {"role": "system", "content": SYSTEM_PROMPT},
    ])
    msg = cl.Message(
        content="Hello! Thanks for contacting ABC Dental Clinic office. How can I help you today?")
    await msg.send()


PATIENT_DATA = [
    {
        "first_name": "Peter",
        "last_name": "Jausovec",
        "phone_number": "123-456-7890",
        "email": "peter@example.org"
    },
    {
        "first_name": "John",
        "last_name": "Doe",
        "phone_number": "555-5555",
        "email": "john@example.org"
    },
]


def save_patient_info(first_name: str, last_name: str, phone_number: str, email: str):
    print(f"Saving patient information for {first_name} {last_name}")

    # Check if the patient already exists
    for patient in PATIENT_DATA:
        if patient["first_name"].lower() == first_name.lower() and patient["last_name"].lower() == last_name.lower():
            return "Patient already exists."

    # Add the patient to the PATIENT_DATA list
    PATIENT_DATA.append({
        "first_name": first_name,
        "last_name": last_name,
        "phone_number": phone_number,
        "email": email
    })

    return "Patient information saved."


def get_patient_info(first_name: str, last_name: str):
    print(f"Getting patient information for {first_name} {last_name}")

    # Check the PAITENT_DATA list for the patient
    for patient in PATIENT_DATA:
        if patient["first_name"].lower() == first_name.lower() and patient["last_name"].lower() == last_name.lower():
            return patient

    return "Patient not found."


def check_appointment_availability(date: str, time: str, appointment_type: str):
    print(
        f"Checking appointment availability for {date} and {appointment_type}")

    # Pick 3 random days and times for demonstration
    available_slots = [
        {"date": "Monday", "time": "1 PM"},
        {"date": "Tuesday", "time": "3 PM"},
        {"date": "Friday", "time": "10 AM"},
    ]

    # Check the schedule for availability
    resp = f"Appointment is not available. Available slots: {available_slots}"
    return resp


def schedule_appointment(date: str, appointment_type: str, time: str, first_name: str, last_name: str):
    print(
        f"Scheduling appointment for {date} and {appointment_type}, {time} for {first_name} {last_name}")

    # Check the schedule for availability
    return "Appointment is scheduled."


def create_appointment_reminder(reminder_type: str, date: str, appointment_type: str, time: str, first_name: str, last_name: str):
    print(
        f"Creating appointment reminder for {reminder_type} for {first_name} {last_name}")

    # Check the schedule for availability
    return "Appointment reminder created."


@cl.on_message
async def on_message(message: cl.Message):
    message_history = cl.user_session.get("message_history")
    message_history.append({"role": "user", "content": message.content})

    response = await client.chat.completions.create(
        messages=message_history,
        tools=TOOLS,
        tool_choice="auto",
        **settings)

    response_message = response.choices[0].message
    message_history.append(response_message)

    if response_message.tool_calls:
        for tool_call in response_message.tool_calls:
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)

            function_response = None
            if function_name == "get_patient_info":
                function_response = get_patient_info(**function_args)
            elif function_name == "save_patient_info":
                function_response = save_patient_info(**function_args)
            elif function_name == "check_appointment_availability":
                function_response = check_appointment_availability(
                    **function_args)
            elif function_name == "schedule_appointment":
                function_response = schedule_appointment(**function_args)
            elif function_name == "create_appointment_reminder":
                function_response = create_appointment_reminder(
                    **function_args)
            else:
                print(f"Function {function_name} not found")

            message_history.append({
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": function_name,
                "content": json.dumps(function_response)
            })

            print(f"Message history: {message_history}")
            print(f"Function response: {function_response}")

            response = await client.chat.completions.create(
                messages=message_history,
                # tools=TOOLS,
                # tool_choice="auto",
                **settings)
            await cl.Message(content=response.choices[0].message.content).send()

    elif response_message.role == "assistant":
        message_history.append(
            {"role": "assistant", "content": response.choices[0].message.content})
        await cl.Message(content=response.choices[0].message.content).send()
