import datetime

def write_log(message):
    with open("log.txt", "a") as file:
        time = datetime.datetime.now()
        file.write(f"{time} - {message}\n")

def read_logs():
    try:
        with open("log.txt", "r") as file:
            print("\n--- Logs ---")
            print(file.read())
    except FileNotFoundError:
        print("No logs found.")

def main():
    while True:
        print("\n1. Write Log")
        print("2. Read Logs")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            msg = input("Enter log message: ")
            write_log(msg)
        elif choice == "2":
            read_logs()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

main()