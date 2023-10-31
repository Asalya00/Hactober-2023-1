# Create a dictionary to store the timetable
timetable = {}

def display_timetable():
    print("Timetable:")
    for day, events in timetable.items():
        print(day)
        for time, event in events.items():
            print(f"  {time}: {event}")

def add_event():
    day = input("Enter the day (e.g., Monday, Tuesday, etc.): ")
    time = input("Enter the time (e.g., 9:00 AM, 2:30 PM, etc.): ")
    event = input("Enter the event: ")

    if day in timetable:
        timetable[day][time] = event
    else:
        timetable[day] = {time: event}

def remove_event():
    day = input("Enter the day to remove an event from: ")
    if day in timetable:
        time = input("Enter the time of the event to remove: ")
        if time in timetable[day]:
            del timetable[day][time]
        else:
            print("Event not found at that time.")
    else:
        print("No events found for that day.")

while True:
    print("\nOptions:")
    print("1. Display Timetable")
    print("2. Add Event")
    print("3. Remove Event")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_timetable()
    elif choice == "2":
        add_event()
    elif choice == "3":
        remove_event()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
