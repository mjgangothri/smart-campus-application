"""
COMPREHENSIVE EXAMPLE SCRIPT
Demonstrates all 8 modules of Smart Campus Information System
Run this to see all features in action
"""

import os
import sys

# Add modules to path
modules_dir = os.path.join(os.path.dirname(__file__), "modules")
sys.path.insert(0, modules_dir)

def example_q1_student_registration():
    """Example: Q1 - Student Registration and Grade Evaluation"""
    print("\n" + "="*70)
    print("EXAMPLE 1: STUDENT REGISTRATION AND GRADE EVALUATION")
    print("="*70)
    
    from modules.student_registration import register_student_and_evaluate
    
    # Simulated example (no user input)
    print("\nSimulated student registration:")
    print("Student: Priya, Score: 82")
    print("Expected: Grade B, Remark: Very Good")
    
    # You can also run interactive: register_student_and_evaluate()

def example_q2_course_enrollment():
    """Example: Q2 - Course Enrollment Management"""
    print("\n" + "="*70)
    print("EXAMPLE 2: COURSE ENROLLMENT MANAGEMENT SYSTEM")
    print("="*70)
    
    # Simulated example
    courses = [
        ("Mathematics", 4),
        ("Physics", 3),
        ("Chemistry", 3)
    ]
    
    print("\nEnrolled Courses:")
    for course, credits in courses:
        print(f"  {course}: {credits} credits")
    
    total_credits = sum(credit for _, credit in courses)
    print(f"\nTotal courses: {len(courses)}")
    print(f"Total credits: {total_credits}")

def example_q3_student_records():
    """Example: Q3 - Student Record Data Management"""
    print("\n" + "="*70)
    print("EXAMPLE 3: STUDENT RECORD DATA MANAGEMENT")
    print("="*70)
    
    # Simulated data structures example
    students = [
        {"name": "Priya", "age": 20, "grades": [85, 90, 78]},
        {"name": "Rahul", "age": 21, "grades": [72, 88, 91]},
        {"name": "Anita", "age": 19, "grades": [95, 89, 92]},
    ]
    
    print("\nStudent Records:")
    for student in students:
        avg = sum(student["grades"]) / len(student["grades"])
        print(f"{student['name']:<15} Age: {student['age']:<2} Avg Grade: {avg:.1f}")
    
    # Event participation using sets
    event_A = {"Priya", "Rahul", "Anita", "Kiran"}
    event_B = {"Rahul", "Anita", "Sneha"}
    
    common = event_A & event_B
    all_participants = event_A | event_B
    
    print(f"\nEvent Participation:")
    print(f"  Common in A & B: {common}")
    print(f"  All participants: {all_participants}")

def example_q4_search_sort():
    """Example: Q4 - Sorting and Searching"""
    print("\n" + "="*70)
    print("EXAMPLE 4: SORTING AND SEARCHING STUDENT IDS")
    print("="*70)
    
    from modules.student_search_sort import bubble_sort, selection_sort, linear_search, binary_search
    
    student_ids = [105, 102, 110, 108, 101, 115]
    
    print(f"\nOriginal IDs: {student_ids}")
    
    sorted_ids = bubble_sort(student_ids.copy())
    print(f"Sorted (Bubble Sort): {sorted_ids}")
    
    # Search example
    target = 108
    idx = linear_search(sorted_ids, target)
    print(f"\nSearch for ID {target}:")
    print(f"  Linear Search: Index {idx} (ID: {sorted_ids[idx]})")
    
    idx = binary_search(sorted_ids, target)
    print(f"  Binary Search: Index {idx} (ID: {sorted_ids[idx]})")

def example_q5_fee_calculation():
    """Example: Q5 - Student Fee Calculation"""
    print("\n" + "="*70)
    print("EXAMPLE 5: STUDENT FEE CALCULATION")
    print("="*70)
    
    from modules.fee_calculation import calculate_fee
    
    print("\nFee Calculation Examples:")
    
    # Case 1: Tuition only
    total1 = calculate_fee(50000)
    print(f"\n1. Tuition Only: ₹ {total1:,}")
    
    # Case 2: Tuition + Hostel
    total2 = calculate_fee(50000, hostel_fee=30000)
    print(f"2. Tuition + Hostel: ₹ {total2:,}")
    
    # Case 3: All components
    total3 = calculate_fee(50000, hostel_fee=30000, transportation_fee=10000)
    print(f"3. Tuition + Hostel + Transport: ₹ {total3:,}")

def example_q6_file_management():
    """Example: Q6 - File Handling"""
    print("\n" + "="*70)
    print("EXAMPLE 6: FILE HANDLING - ACADEMIC RECORDS")
    print("="*70)
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    records_file = os.path.join(base_path, "student_records.txt")
    
    if os.path.exists(records_file):
        print(f"\nReading from {os.path.basename(records_file)}:")
        with open(records_file, "r") as f:
            lines = f.readlines()[:4]  # First 4 lines
            for line in lines:
                print(f"  {line.rstrip()}")
        print("  ...")
    else:
        print(f"Sample file not found. Create using main.py (Q6 option)")

def example_q7_directory_scanning():
    """Example: Q7 - Directory Scanning"""
    print("\n" + "="*70)
    print("EXAMPLE 7: DIRECTORY SCANNING WITH EXCEPTION HANDLING")
    print("="*70)
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    projects_dir = os.path.join(base_path, "Projects")
    
    print(f"\nScanning: {projects_dir}")
    print("-"*70)
    
    if os.path.exists(projects_dir):
        for root, dirs, files in os.walk(projects_dir):
            level = root.replace(projects_dir, "").count(os.sep)
            indent = "  " * level
            folder = os.path.basename(root) or "Projects"
            print(f"{indent}📁 {folder}/")
            
            subindent = "  " * (level + 1)
            for file in files:
                print(f"{subindent}📄 {file}")
    else:
        print("Projects directory not found")

def example_q8_performance_analytics():
    """Example: Q8 - Performance Analytics"""
    print("\n" + "="*70)
    print("EXAMPLE 8: STUDENT PERFORMANCE ANALYSIS")
    print("="*70)
    
    try:
        import pandas as pd
        import numpy as np
        
        # Sample data
        data = {
            'Name': ['Priya', 'Rahul', 'Anita', 'Vikram', 'Sneha'],
            'Math': [85, 72, 95, 88, 78],
            'Science': [90, 88, 89, 92, 85],
            'English': [78, 91, 92, 85, 88]
        }
        
        df = pd.DataFrame(data)
        scores = df[["Math", "Science", "English"]].to_numpy()
        
        print("\nStudent Performance Data:")
        print(df.to_string(index=False))
        
        print("\n\nStatistical Analysis:")
        mean_scores = np.mean(scores, axis=0)
        median_scores = np.median(scores, axis=0)
        std_dev = np.std(scores, axis=0)
        
        subjects = ["Math", "Science", "English"]
        for i, subject in enumerate(subjects):
            print(f"\n{subject}:")
            print(f"  Mean:   {mean_scores[i]:.2f}")
            print(f"  Median: {median_scores[i]:.2f}")
            print(f"  Std:    {std_dev[i]:.2f}")
        
        print("\n\nTop Performers:")
        top_math = df.loc[df["Math"].idxmax(), "Name"]
        top_sci = df.loc[df["Science"].idxmax(), "Name"]
        top_eng = df.loc[df["English"].idxmax(), "Name"]
        print(f"  Math:    {top_math}")
        print(f"  Science: {top_sci}")
        print(f"  English: {top_eng}")
        
    except ImportError:
        print("\nNumPy/Pandas not available. Install with: pip install numpy pandas")

def main():
    """Run all examples"""
    print("\n")
    print("╔" + "="*68 + "╗")
    print("║" + " "*15 + "SMART CAMPUS INFORMATION SYSTEM" + " "*22 + "║")
    print("║" + " "*20 + "COMPREHENSIVE EXAMPLES" + " "*27 + "║")
    print("╚" + "="*68 + "╝")
    
    try:
        example_q1_student_registration()
        example_q2_course_enrollment()
        example_q3_student_records()
        example_q4_search_sort()
        example_q5_fee_calculation()
        example_q6_file_management()
        example_q7_directory_scanning()
        example_q8_performance_analytics()
        
        print("\n" + "="*70)
        print("✅ ALL EXAMPLES COMPLETED SUCCESSFULLY!")
        print("="*70)
        print("\nTo run the interactive system, execute: python main.py")
        print("\nFor more information, see README.md and QUICKSTART.md")
        print("="*70 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error running examples: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
