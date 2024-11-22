TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_patient_info",
            "description": "Get the patient information by their first and last name.",
            "parameters": {
                "type": "object",
                "properties": {
                    "first_name": {
                        "type": "string",
                        "description": "Patients first name",
                    },
                    "last_name": {
                        "type": "string",
                        "description": "Patients last name",
                    },
                },
                "required": ["first_name", "last_name"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "save_patient_info",
            "description": "Stores the patient information in the system.",
            "parameters": {
                "type": "object",
                "properties": {
                    "first_name": {
                        "type": "string",
                        "description": "Patients first name",
                    },
                    "last_name": {
                        "type": "string",
                        "description": "Patients last name",
                    },
                    "phone_number": {
                        "type": "string",
                        "description": "Patients phone number",
                    },
                    "email": {
                        "type": "string",
                        "description": "Patients email",
                    },
                },
                "required": ["first_name", "last_name", "phone_number", "email"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "check_appointment_availability",
            "description": "Checks whether the desired date and time is available or not and returns alternative slots.",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "Date of the appointment",
                    },
                    "time": {
                        "type": "string",
                        "description": "Time of the appointment",
                    },
                    "appointment_type": {
                        "type": "string",
                        "description": "Type of the appointment (e.g. routine check-up, cleaning, filling)",
                    },
                },
                "required": ["date", "time", "appointment_type"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "schedule_appointment",
            "description": "Schedules an appointment for the patient and stores it in the system.",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "Date of the appointment",
                    },
                    "time": {
                        "type": "string",
                        "description": "Time of the appointment",
                    },
                    "appointment_type": {
                        "type": "string",
                        "description": "Type of the appointment (e.g. routine check-up, cleaning, filling)",
                    },
                    "first_name": {
                        "type": "string",
                        "description": "Patients first name",
                    },
                    "last_name": {
                        "type": "string",
                        "description": "Patients last name",
                    },
                },
                "required": ["date", "appointment_type", "time", "first_name", "last_name"],
            },
        },
    },

    {
        "type": "function",
        "function": {
            "name": "create_appointment_reminder",
            "description": "Creates an appointment reminder for the patients appontment.",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "Date of the appointment",
                    },
                    "time": {
                        "type": "string",
                        "description": "Time of the appointment",
                    },
                    "appointment_type": {
                        "type": "string",
                        "description": "Type of the appointment (e.g. routine check-up, cleaning, filling)",
                    },
                    "first_name": {
                        "type": "string",
                        "description": "Patients first name",
                    },
                    "last_name": {
                        "type": "string",
                        "description": "Patients last name",
                    },
                    "reminder_type": {
                        "type": "string",
                        "description": "Type of reminder (e.g. call, text, email)",
                    },
                },
                "required": ["date", "appointment_type", "time", "first_name", "last_name", "reminder_type"],
            },
        },
    },

]
