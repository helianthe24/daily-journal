from journal.entry import create_entry

def run_cli():
    print("Welcome to your digital journal.")
    date = input("Enter the date (YYYY-MM-DD) or leave blank for today: ")
    create_entry(date)
