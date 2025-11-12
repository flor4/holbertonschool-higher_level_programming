import os


def generate_invitations(template, attendees):
    """
    Generates personalized invitation files based
    on a template and a list of attendee dictionaries.

    Args:
        template (str): The invitation template with placeholders.
        attendees (list): A list of dictionaries with attendee data.

    Returns:
        None
    """
    # --- Step 1: Validate input types ---
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # --- Step 2: Handle empty inputs ---
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # --- Step 3: Process each attendee ---
    for idx, attendee in enumerate(attendees, start=1):
        # Use .get() with fallback "N/A" if a key is missing or value is None
        name = attendee.get("name") or "N/A"
        event_title = attendee.get("event_title") or "N/A"
        event_date = attendee.get("event_date") or "N/A"
        event_location = attendee.get("event_location") or "N/A"

        # Replace placeholders in the template
        personalized = template
        personalized = personalized.replace("{name}", name)
        personalized = personalized.replace("{event_title}", event_title)
        personalized = personalized.replace("{event_date}", event_date)
        personalized = personalized.replace("{event_location}", event_location)

        # --- Step 4: Generate output file ---
        output_filename = f"output_{idx}.txt"
        try:
            with open(output_filename, "w", encoding="utf-8") as f:
                f.write(personalized)
            print(f"Generated: {output_filename}")
        except Exception as e:
            print(f"Error writing to {output_filename}: {e}")
