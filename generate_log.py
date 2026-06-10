from datetime import datetime
import os

def generate_log(data):
    """Generate a log file from a list of entries.

    Takes a list of log entries, writes each one to a timestamped .txt file,
    and returns the filename.

    Args:
        data (list): A list of strings to write as log entries.

    Returns:
        str: The name of the generated log file.

    Raises:
        ValueError: If data is not a list.
    """

    # STEP 1: Validate input
    if not isinstance(data, list):
        raise ValueError("data must be a list")

    # STEP 2: Generate filename with today's date
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write log entries to the file
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print confirmation message
    print(f"Log written to {filename}")

    return filename