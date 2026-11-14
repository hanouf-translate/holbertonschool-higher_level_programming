#!/usr/bin/python3
""" generate_invitations function implementaion """

import logging 
import os
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

def generate_invitations(template, attendees):
    """ Python function that generates personalized invitation files from a template with placeholders and a list of objects.
     Each output file should be named sequentially, starting from 1."""
    if not isinstance(template, str):
            logging.error(
                f"Invalid input: template must be a string, got {type(template).__name__}."
            )
            return

    if not isinstance(attendees, list) or not all(
        isinstance(item, dict) for item in attendees
    ):
        logging.error(
            f"Invalid input: attendees must be a list of dictionaries, got {type(attendees).__name__}."
        )
        return

    if not template.strip():
        logging.error("Template is empty, no output file generated")
        return
    
    if not attendees:
        logging.error("Template is empty, no output file generated")
        return
    
    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        processed_template = template

        for key in placeholders:
                    value = attendee.get(key)
                    # Replace missing keys or None values with "N/A"
                    replacement = str(value) if value is not None else "N/A"
                    processed_template = processed_template.replace(
                        f"{{{key}}}", replacement
                    )
        output_filename = f"output_{index}.txt"
        try:
            if os.path.exists(output_filename):
                logging.warning(
                    f"File {output_filename} already exists and will be overwritten."
                )

            with open(output_filename, "w", encoding="utf-8") as output_file:
                output_file.write(processed_template)
        except OSError as e:
            logging.error(f"Failed to write {output_filename}: {e}")

    

