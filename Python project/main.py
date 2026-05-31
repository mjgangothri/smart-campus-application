"""
SMART CAMPUS INFORMATION SYSTEM
Main Dashboard Application
Dayananda Sagar College of Engineering

This is the central control interface that provides access to all 8 laboratory modules
for student information management, academic records, and performance analysis.
"""

import os
import sys

# Add modules to path
modules_dir = os.path.join(os.path.dirname(__file__), "modules")
sys.path.insert(0, modules_dir)

# Import all modules
from modules.student_registration import register_student_and_evaluate
from modules.course_enrollment import manage_course_enrollment
from modules.student_records import manage_student_records
from modules.student_search_sort import sorting_and_searching_demo
from modules.fee_calculation import manage_student_fees
from modules.file_management import manage_academic_records
from modules.directory_scanning import scan_directory_interactive
from modules.performance_analytics import analyze_student_performance


def display_main_menu():
    """Display the main dashboard menu"""
    print("\n" + "="*70)
    print("SMART CAMPUS INFORMATION SYSTEM - MAIN DASHBOARD")
    print("Dayananda Sagar College of Engineering")
    print("="*70)
    print("\n📚 LABORATORY MODULES:\n")
    print("  Q1  → Student Registration and Grade Evaluation")
    print("  Q2  → Course Enrollment Management System")
    print("  Q3  → Student Record Data Management")
    print("  Q4  → Sorting and Searching of Student IDs")
    print("  Q5  → Student Fee Calculation")
    print("  Q6  → File Handling for Academic Records")
    print("  Q7  → Directory Scanning with Exception Handling")
    print("  Q8  → Student Performance Analysis")
    print("\n📌 DEMO OPTIONS:\n")
    print("  Q9  → Demo - Predefined Fee Calculation Examples")
    print("  Q10 → Demo - Scan Project Directory")
    print("\n  0   → Exit System\n")
    print("="*70)


def run_demo_fee_calculation():
    """Demo mode: Run predefined fee calculation examples"""
    print("\n" + "="*70)
    print("DEMO: PREDEFINED FEE CALCULATION EXAMPLES")
    print("="*70)
    
    from modules.fee_calculation import calculate_fee
    
    # Example students with predefined data
    students_demo = [
        {
            "name": "Priya Sharma",
            "student_id": "DS001",
            "semester": 4,
            "courses": 5,
            "scholarship": 10000
        },
        {
            "name": "Rahul Kumar",
            "student_id": "DS002",
            "semester": 2,
            "courses": 4,
            "scholarship": 0
        },
        {
            "name": "Anita Singh",
            "student_id": "DS003",
            "semester": 6,
            "courses": 6,
            "scholarship": 15000
        }
    ]
    
    print("\nCalculating fees for demo students:\n")
    
    for student in students_demo:
        # Calculate tuition fee based on semester and courses
        tuition_fee = student["semester"] * 10000 + student["courses"] * 2000
        total_fee = calculate_fee(
            tuition_fee=tuition_fee,
            hostel_fee=5000,
            transportation_fee=student["scholarship"] > 0 and 0 or 2000
        )
        total_fee = max(0, total_fee - student["scholarship"])
        print(f"Student: {student['name']} (ID: {student['student_id']})")
        print(f"  Semester: {student['semester']} | Courses: {student['courses']}")
        print(f"  Scholarship: ₹{student['scholarship']}")
        print(f"  Total Fee: ₹{total_fee}\n")


def run_demo_directory_scan():
    """Demo mode: Scan the Projects directory"""
    print("\n" + "="*70)
    from modules.directory_scanning import scan_directory

    project_dir = os.path.join(os.path.dirname(__file__), "Projects")

    if os.path.exists(project_dir):
        print(f"\nScanning directory: {project_dir}\n")
        scan_directory(project_dir)
    else:
        print(f"\n❌ Projects directory not found at: {project_dir}")


def main():
    """Main dashboard controller"""
    while True:
        display_main_menu()
        choice = input("Enter your choice (Q1-Q10 or 0 to exit): ").strip().upper()
        
        try:
            if choice == "Q1":
                print("\n" + "="*70)
                print("Q1: STUDENT REGISTRATION AND GRADE EVALUATION")
                print("="*70)
                register_student_and_evaluate()
                
            elif choice == "Q2":
                print("\n" + "="*70)
                print("Q2: COURSE ENROLLMENT MANAGEMENT SYSTEM")
                print("="*70)
                manage_course_enrollment()
                
            elif choice == "Q3":
                print("\n" + "="*70)
                print("Q3: STUDENT RECORD DATA MANAGEMENT")
                print("="*70)
                manage_student_records()
                
            elif choice == "Q4":
                print("\n" + "="*70)
                print("Q4: SORTING AND SEARCHING OF STUDENT IDS")
                print("="*70)
                sorting_and_searching_demo()
                
            elif choice == "Q5":
                print("\n" + "="*70)
                print("Q5: STUDENT FEE CALCULATION")
                print("="*70)
                manage_student_fees()
                
            elif choice == "Q6":
                print("\n" + "="*70)
                print("Q6: FILE HANDLING FOR ACADEMIC RECORDS")
                print("="*70)
                base_path = os.path.dirname(__file__)
                manage_academic_records(base_path)
                
            elif choice == "Q7":
                print("\n" + "="*70)
                print("Q7: DIRECTORY SCANNING WITH EXCEPTION HANDLING")
                print("="*70)
                scan_directory_interactive()
                
            elif choice == "Q8":
                print("\n" + "="*70)
                print("Q8: STUDENT PERFORMANCE ANALYSIS")
                print("="*70)
                analyze_student_performance()
                
            elif choice == "Q9":
                run_demo_fee_calculation()
                
            elif choice == "Q10":
                run_demo_directory_scan()
                
            elif choice == "0":
                print("\n" + "="*70)
                print("Thank you for using Smart Campus Information System!")
                print("Goodbye!")
                print("="*70 + "\n")
                break
            
            else:
                print("\n❌ Invalid choice! Please select Q1-Q10 or 0 to exit.\n")
                continue
            
            # Prompt to continue
            input("\nPress Enter to continue...")
            
        except KeyboardInterrupt:
            print("\n\n⚠️  Program interrupted by user.")
            print("Thank you for using Smart Campus Information System!")
            break
        except Exception as e:
            print(f"\n❌ An error occurred: {str(e)}")
            print("Please try again or select a different option.")
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
