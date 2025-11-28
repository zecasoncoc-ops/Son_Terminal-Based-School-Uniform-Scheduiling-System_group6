# School Uniform Scheduling System 
import datetime 

print("=== Welcome to School Uniform Scheduling System ===")

# Data storage
students = {}  # name : password
schedules = []

staff_password = "Phinmaadmin1234"

MAX_PER_SLOT_TIME = 30

while True:
    print("\nSelect User Type:")
    print("1. Student")
    print("2. Business Center Staff")
    print("3. Exit")

    user = input("Please Enter choice: ")

    # STUDENT MENU
    if user == "1":
        while True:
            print("\n--- STUDENT MENU ---")
            print("1. Register")
            print("2. Book a Schedule")
            print("3. View Schedule")
            print("4. Cancel Schedule")
            print("5. Back to Main Menu")
            choice = input("Enter choice: ")
            
            # Register
            if choice == "1":
                name = input("Enter your name: ")
                if name in students:
                    print("This name is already registered.")
                else:
                    password = input("Set your password: ")
                    students[name] = password
                    print("Registration successful! You can now log in.")
                    
            # Book schedule
            elif choice == "2":
                if len(students) == 0:
                    print("No registered students yet.")
                else:
                    name = input("Enter your registered name: ")
                    password = input("Enter your password: ")
                    if name in students and students[name] == password:

                        already_booked = False
                        for s in schedules:
                            if s["name"] == name:
                                already_booked = True
                                break

                        if already_booked:
                            print("You already have a booked schedule. You cannot book again.")
                            continue

                        date_input = input("Enter date (e.g. Nov 12 2025): ")
                        time = input("Enter time (open only 8 AM to 5 PM): ")

                        # Date validation
                        try:
                            date_obj = datetime.datetime.strptime(date_input, "%b %d %Y").date()
                            today = datetime.date.today()
                            if date_obj < today:
                                print("Invalid date! That date has already passed.")
                                continue
                        except ValueError:
                            print("Invalid date please Include the year 'Nov 12 2025'.")
                            continue

                        valid_times = ["8 AM", "9 AM", "10 AM", "11 AM", "12 PM",
                                       "1 PM", "2 PM", "3 PM", "4 PM", "5 PM"]
                        if time not in valid_times:
                            print("Invalid time! Open hours are only 8 AM to 5 PM.")
                            continue

                        count = 0
                        for s in schedules:
                            if s["date"] == date_input and s["time"] == time:
                                count += 1

                        if count >= MAX_PER_SLOT_TIME:
                            print("Sorry, this time slot is full (limit: 30 students). Please choose another time.")
                        else:
                            schedules.append({
                                "name": name,
                                "date": date_input,
                                "time": time,
                                "status": "Booked",
                                "updated_at": datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")
                            })
                            print(f"Schedule booked successfully! ({count + 1}/30 students in this time slot)")
                    else:
                        print("Invalid name or password!")
                        
            # View schedule
            elif choice == "3":
                name = input("Enter your name: ")
                password = input("Enter your password: ")
                if name in students and students[name] == password:
                    found = False
                    for s in schedules:
                        if s["name"] == name:
                            print(f"Schedule for {s['name']}: {s['date']} at {s['time']} - Status: {s['status']} (Updated: {s['updated_at']})")
                            found = True
                    if not found:
                        print("No schedule found.")
                else:
                    print("Invalid name or password!")
                    
            # Cancel schedule
            elif choice == "4":
                name = input("Enter your name: ")
                password = input("Enter your password: ")
                if name in students and students[name] == password:
                    found = False
                    for s in schedules:
                        if s["name"] == name:
                            confirm = input("Are you sure you want to cancel your schedule? (yes/no): ").lower()
                            if confirm == "yes":
                                schedules.remove(s)
                                print("Schedule cancelled successfully!")
                            else:
                                print("Cancellation cancelled. Returning to menu.")
                            found = True
                            break
                    if not found:
                        print("No schedule found to cancel.")
                else:
                    print("Invalid name or password!")
                    
            # Back to menu
            elif choice == "5":
                break
            else:
                print("Invalid choice! Please try again.")

    # BUSINESS CENTER STAFF MENU
    elif user == "2":
        password = input("Enter staff password: ")
        if password != staff_password:
            print("Incorrect password! Access denied.")
            continue

        while True:
            print("\n--- BUSINESS CENTER STAFF MENU ---")
            print("1. View All Schedules")
            print("2. Update Schedule Status")
            print("3. Back to Main Menu")
            choice = input("Enter choice: ")
            
            # View All Schedules
            if choice == "1":
                if len(schedules) == 0:
                    print("No schedules found.")
                else:
                    for s in schedules:
                        print(f"{s['name']} - {s['date']} at {s['time']} - Status: {s['status']} (Updated: {s['updated_at']})")
                        
            #  Update Schedule Status            
            elif choice == "2":
                name = input("Enter student name to update: ")
                found = False
                for s in schedules:
                    if s["name"] == name:
                        print(f"Current status: {s['status']}")
                        new_status = input("Enter new status (Claimed/Rescheduled): ")
                        s["status"] = new_status
                        s["updated_at"] = datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")
                        print(f"Status updated successfully at {s['updated_at']}!")
                        found = True
                        break
                if not found:
                    print("Student not found in schedule list.")
                    
            # Back to Main Menu        
            elif choice == "3":
                break
            else:
                print("Invalid choice! Please try again.")

    elif user == "3":
        print("Thank you for using the system!")
        break
    else:
        print("Invalid option! Please try again.")