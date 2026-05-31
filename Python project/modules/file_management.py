# Q6: File Handling for Student Academic Records
import os

def manage_academic_records(base_path):
    """
    Manages student academic records in files
    """
    print("\n" + "="*50)
    print("    FILE HANDLING - ACADEMIC RECORDS")
    print("="*50)
    
    records_file = os.path.join(base_path, "student_records.txt")
    
    print("\nOptions:")
    print("1. Write new records to file")
    print("2. Read records from file")
    print("3. Generate report from file")
    print("4. Add new record to file")
    
    choice = input("\nSelect option (1-4): ").strip()
    
    if choice == "1":
        write_student_records(records_file)
    elif choice == "2":
        read_student_records(records_file)
    elif choice == "3":
        generate_report_from_file(records_file)
    elif choice == "4":
        add_new_record(records_file)
    else:
        print("Invalid option!")


def write_student_records(filepath):
    """Write predefined student records to file"""
    print("\n" + "-"*50)
    print("            WRITING RECORDS TO FILE")
    print("-"*50)
    
    try:
        with open(filepath, "w") as file:
            file.write("ID,Name,Marks\n")
            file.write("101,Arjun,85\n")
            file.write("102,Meera,92\n")
            file.write("103,Ravi,76\n")
            file.write("104,Anita,89\n")
            file.write("105,Vikram,95\n")
        print(f"✓ Student records written to {os.path.basename(filepath)}")
    except Exception as e:
        print(f"Error writing to file: {e}")


def read_student_records(filepath):
    """Read student records from file"""
    print("\n" + "-"*50)
    print("            READING RECORDS FROM FILE")
    print("-"*50)
    
    try:
        if not os.path.exists(filepath):
            print(f"File '{os.path.basename(filepath)}' not found.")
            print("Please write records first (Option 1).")
            return []
        
        with open(filepath, "r") as file:
            records = file.readlines()
        
        if records:
            print("\nStudent Records:")
            for record in records:
                print(record.strip())
            return records
        else:
            print("No records found in file.")
            return []
            
    except Exception as e:
        print(f"Error reading file: {e}")
        return []


def add_new_record(filepath):
    """Add new student record to file"""
    print("\n" + "-"*50)
    print("            ADD NEW RECORD")
    print("-"*50)
    
    try:
        # Check if file exists, if not create with header
        if not os.path.exists(filepath):
            with open(filepath, "w") as file:
                file.write("ID,Name,Marks\n")
        
        student_id = input("Enter student ID: ").strip()
        name = input("Enter student name: ").strip()
        
        try:
            marks = float(input("Enter marks (0-100): "))
            if marks < 0 or marks > 100:
                print("Invalid marks! Must be between 0 and 100.")
                return
        except ValueError:
            print("Invalid input! Marks must be a number.")
            return
        
        with open(filepath, "a") as file:
            file.write(f"{student_id},{name},{int(marks)}\n")
        
        print(f"✓ Record added successfully!")
        
    except Exception as e:
        print(f"Error adding record: {e}")


def generate_report_from_file(filepath):
    """Generate report from file data"""
    print("\n" + "-"*50)
    print("            GENERATING REPORT FROM FILE")
    print("-"*50)
    
    try:
        if not os.path.exists(filepath):
            print(f"File '{os.path.basename(filepath)}' not found.")
            print("Please write records first (Option 1).")
            return
        
        with open(filepath, "r") as file:
            records = file.readlines()
        
        if len(records) <= 1:
            print("No student records found in file.")
            return
        
        # Process records
        total_students = 0
        total_marks = 0
        highest_marks = -1
        top_student = ""
        student_details = []
        
        for record in records[1:]:  # Skip header
            parts = record.strip().split(",")
            if len(parts) >= 3:
                try:
                    student_id = parts[0]
                    name = parts[1]
                    marks = float(parts[2])
                    
                    student_details.append((student_id, name, marks))
                    total_students += 1
                    total_marks += marks
                    
                    if marks > highest_marks:
                        highest_marks = marks
                        top_student = name
                except ValueError:
                    continue
        
        if total_students > 0:
            average_marks = total_marks / total_students
            
            print("\nReport Summary:")
            print(f"Total Students:   {total_students}")
            print(f"Average Marks:    {average_marks:.2f}")
            print(f"Top Student:      {top_student} ({highest_marks:.1f} marks)")
            
            print("\nDetailed Breakdown:")
            for sid, name, marks in sorted(student_details, key=lambda x: x[2], reverse=True):
                print(f"  {sid} - {name:<20} {marks:>6.1f}")
        else:
            print("No valid records to process.")
        
    except Exception as e:
        print(f"Error generating report: {e}")
