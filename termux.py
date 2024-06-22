import subprocess
import os
import json
import uuid

# Dictionary to keep track of processes
process_dict = {}

def load_data():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"users": {}}

def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

def start_process():
    appstate = input("Enter your appstate (JSON format): ")
    target_id = input("Enter your target ID: ")
    message = input("Enter your message: ")
    delay_time = input("Enter delay time: ")

    # Convert appstate from string to dictionary
    try:
        appstate = json.loads(appstate)
    except json.JSONDecodeError:
        print("Invalid JSON format for appstate. Please try again.")
        return

    unique_id = str(uuid.uuid4())
    process_data = {
        "appstate": appstate,
        "target_id": target_id,
        "message": message,
        "time": delay_time
    }

    data = load_data()
    data["users"][unique_id] = process_data
    save_data(data)

    # Example process, you can change this to the actual process you need to run
    process = subprocess.Popen(["python3", "-c", f"while True: print('{message}'); import time; time.sleep({delay_time})"], 
                                stdout=subprocess.PIPE, 
                                stderr=subprocess.PIPE, 
                                preexec_fn=os.setsid)
    process_dict[process.pid] = process
    print(f"Process started with PID: {process.pid} and Unique ID: {unique_id}")

def see_process():
    # Placeholder function to see processes
    print("See process functionality is not implemented yet.")

def stop_process():
    # Placeholder function to stop a process
    print("Stop process functionality is not implemented yet.")

while True:
    print("\n1. Start process\n2. See process\n3. Stop process\n4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        start_process()
    elif choice == '2':
        see_process()
    elif choice == '3':
        stop_process()
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice, please try again.")
  
