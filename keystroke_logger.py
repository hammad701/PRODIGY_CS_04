from datetime import datetime

def get_user_consent():
    print("ETHICAL NOTICE")
    print("This program records keystrokes ONLY inside this application.")
    print("No system-wide monitoring is performed.")
    consent = input("Do you agree to proceed? (yes/no): ").lower()
    return consent == "yes"

def log_keystrokes():
    log_file = "keystrokes.log"

    print("\nStart typing. Type 'EXIT' to stop logging.\n")

    with open(log_file, "a") as file:
        while True:
            user_input = input("> ")

            if user_input.upper() == "EXIT":
                print("Logging stopped.")
                break

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"[{timestamp}] {user_input}\n")

if __name__ == "__main__":
    if get_user_consent():
        log_keystrokes()
    else:
        print("Permission not granted. Program terminated.")
