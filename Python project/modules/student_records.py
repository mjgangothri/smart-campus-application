# Q3: Student Record Data Management using Data Structures
def manage_student_records():
    """
    Manages student records using lists, dictionaries, and sets
    """
    print("\n" + "="*50)
    print("    STUDENT RECORD DATA MANAGEMENT")
    print("="*50)
    
    # Step 1 & 2: Input Collection and Record Management
    students = []
    
    print("\nEnter student details. Type 'done' when finished.\n")
    
    while True:
        name = input("Enter student name (or 'done' to finish): ").strip()
        
        if name.lower() == "done":
            break
        
        if not name:
            print("Name cannot be empty!\n")
            continue
        
        try:
            age = int(input(f"Enter age for {name}: "))
            if age < 10 or age > 100:
                print("Invalid age! Please enter a valid age.\n")
                continue
            
            grades_input = input(f"Enter grades for {name} (comma-separated): ").strip()
            grades = [float(g.strip()) for g in grades_input.split(",")]
            
            # Validate grades
            if any(g < 0 or g > 100 for g in grades):
                print("Invalid grades! All grades must be between 0 and 100.\n")
                continue
            
            students.append({
                "name": name,
                "age": age,
                "grades": grades
            })
            print(f"✓ Student '{name}' added successfully.\n")
            
        except ValueError:
            print("Invalid input! Please enter valid age and grades.\n")
            continue
    
    # Display records
    if students:
        print("\n" + "-"*50)
        print("            STUDENT RECORDS")
        print("-"*50)
        for student in students:
            avg_grade = sum(student["grades"]) / len(student["grades"])
            print(f"Name: {student['name']:<20} Age: {student['age']:<3} Grades: {student['grades']}")
            print(f"Average Grade: {avg_grade:.2f}\n")
    
    # Step 3: Event Participation Analysis using Sets
    event_management(students)
    
    return students


def event_management(students):
    """
    Analyzes student participation in campus events using sets
    """
    if not students:
        return
    
    print("-"*50)
    print("    EVENT PARTICIPATION ANALYSIS")
    print("-"*50)
    
    student_names = {student["name"] for student in students}
    
    # Sample events with participants
    event_A = {"Priya", "Rahul", "Anita", "Kiran"}
    event_B = {"Rahul", "Anita", "Sneha"}
    event_C = {"Priya", "Sneha", "Kiran"}
    
    # Operations on sets
    common_AB = event_A & event_B
    common_all = event_A & event_B & event_C
    all_participants = event_A | event_B | event_C
    only_A = event_A - event_B - event_C
    
    print(f"\nEvent A participants: {event_A}")
    print(f"Event B participants: {event_B}")
    print(f"Event C participants: {event_C}")
    
    print(f"\nCommon participants (A & B): {common_AB}")
    print(f"Common in all events: {common_all}")
    print(f"All participants (A | B | C): {all_participants}")
    print(f"Only Event A: {only_A}")
    print("-"*50)
