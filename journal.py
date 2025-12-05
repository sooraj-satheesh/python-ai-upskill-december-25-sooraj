from datetime import datetime
import csv


def get_journal_message():
    print("Write your journal message: How do you feel today? (happy/sad/neutral)")
    while True:
        msg = input()
        if msg == "" or not (msg == "happy" or msg == "sad" or msg == "neutral"):
            print("invalid answer, try again")
            continue
        else:
            return msg


def msg_to_mood(msg):
    match msg:
        case "happy":
            return "`:)"
        case "sad":
            return ":("
        case "neutral":
            return "`:"


def get_user_name() -> str:
    print("Welcome to the Secret Journal\nEnter your name")
    name = input()
    return name


def create_entry(entry_id):
    msg = get_journal_message()
    mood = msg_to_mood(msg)
    entry = {
        "id": entry_id,
        "message": msg,
        "mood": mood,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    return entry


def save_entry_to_csv(entries):
    fieldnames = ["id", "message", "mood", "timestamp"]
    csv_file_path = "out.csv"
    try:
        with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(entries)
        print(f"Successfully wrote data to {csv_file_path}")
    except IOError:
        print("I/O error occurred while writing the file.")


def load_entries():
    csv_file_path = "out.csv"
    data_as_dicts = []

    try:
        with open(csv_file_path, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data_as_dicts.append(row)

        print(f"Successfully read data from {csv_file_path}")
    except FileNotFoundError:
        print(f"Error: The file {csv_file_path} was not found.")
    except Exception as e:
        print(f"An error occurred during reading: {e}")
    return data_as_dicts


def display_entries(entries):
    for item in entries:
        print(item)


def main():
    entries = []
    get_user_name()
    while True:
        print(
            """What would you like  to  do?
        1. Write a new journal entry 
        2. View saved entries 
        3. Exit 
        Enter your choice:"""
        )
        choice = int(input())
        match choice:
            case 1:
                entry = create_entry(len(entries) + 1)
                entries.append(entry)
                save_entry_to_csv(entries)
            case 2:
                entries = load_entries()
                display_entries(entries)
            case 3:
                exit()


if __name__ == "__main__":
    main()
