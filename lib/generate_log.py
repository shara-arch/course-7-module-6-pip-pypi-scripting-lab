from datetime import datetime
import os
import requests 

def generate_log(log_data):
    # STEP 1: Validate input
    # Fix: Changed parameter to log_data so this check works correctly
    if not isinstance(log_data, list):
        raise ValueError("Input data must be of type 'list'.")

    # STEP 2: Generate a filename with today's date (e.g., "log_20260610.txt")
    current_date = datetime.now().strftime("%Y%m%d")
    filename = f"log_{current_date}.txt"

    # STEP 3: Write the log entries to a file using File I/O
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message with the filename
    print(f"Log written to {filename}")

def fetch_data():
    # Fetches mockup platform data using requests.
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=5)
        if response.status_code == 200:
            return response.json()
    except requests.RequestException:
        pass
    return {}

if __name__ == "__main__":
    # Fetch sample remote data 
    post = fetch_data()
    post_title = post.get("title", "No title found")
    
    # Build out log list array
    sample_logs = [
        "User logged in", 
        "User updated profile", 
        f"Report exported: {post_title}"
    ]
    
    # Execute log generation safely
    generate_log(sample_logs)