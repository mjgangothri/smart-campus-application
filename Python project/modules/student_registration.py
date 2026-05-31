# Q1: Student Registration and Grade Evaluation
def register_student_and_evaluate():
    """
    Accepts student details and evaluates grade using conditional statements
    """
    print("\n" + "="*50)
    print("    STUDENT REGISTRATION AND GRADE EVALUATION")
    print("="*50)
    
    # Step 1: Input collection
    student_name = input("\nEnter student name: ").strip()
    
    try:
        score = float(input("Enter exam score (0-100): "))
        
        # Validate score range
        if score < 0 or score > 100:
            print("Invalid score! Score must be between 0 and 100.")
            return None
        
        # Step 2: Grade evaluation using conditional statements
        if score >= 90 and score <= 100:
            grade = "A"
            remark = "Excellent"
        elif score >= 75:
            grade = "B"
            remark = "Very Good"
        elif score >= 60:
            grade = "C"
            remark = "Good"
        elif score >= 40:
            grade = "D"
            remark = "Average"
        else:
            grade = "F"
            remark = "Needs Improvement"
        
        # Step 3: Output display
        print("\n" + "-"*50)
        print("            STUDENT REPORT")
        print("-"*50)
        print(f"Name:                  {student_name}")
        print(f"Score:                 {score}")
        print(f"Grade:                 {grade}")
        print(f"Performance Remark:    {remark}")
        print("-"*50)
        
        return {
            'name': student_name,
            'score': score,
            'grade': grade,
            'remark': remark
        }
        
    except ValueError:
        print("Invalid input! Score must be a number.")
        return None
