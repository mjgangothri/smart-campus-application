# Q2: Course Enrollment Management System
def manage_course_enrollment():
    """
    Manages course enrollment using loops and control statements
    """
    print("\n" + "="*50)
    print("    COURSE ENROLLMENT MANAGEMENT SYSTEM")
    print("="*50)
    
    # Step 1: Input collection with loop
    courses = []
    max_courses = 5
    
    print(f"\nEnter course details (Maximum {max_courses} courses allowed)")
    print("Type 'done' to finish enrollment.\n")
    
    while True:
        # Check maximum limit using break
        if len(courses) >= max_courses:
            print(f"\nMaximum course limit ({max_courses}) reached!")
            break
        
        course_name = input("Enter course name (or 'done' to finish): ").strip()
        
        # Allow user to finish
        if course_name.lower() == "done":
            break
        
        # Validate course name
        if not course_name:
            print("Course name cannot be empty! Skipping entry...\n")
            continue
        
        credits = input("Enter credit value: ").strip()
        
        # Step 2: Validation using if-elif-else
        if not credits.isdigit():
            print("Invalid credit value! Skipping entry...\n")
            continue
        
        credits = int(credits)
        
        if credits <= 0:
            print("Credit must be positive! Skipping entry...\n")
            continue
        
        if credits > 10:
            print("Credit value too high! Maximum 10 credits allowed. Skipping...\n")
            continue
        
        # Valid entry → add to list
        courses.append((course_name, credits))
        print(f"✓ Course '{course_name}' with {credits} credits added.\n")
    
    # Step 3: Output display
    if courses:
        print("\n" + "-"*50)
        print("            ENROLLMENT REPORT")
        print("-"*50)
        total_credits = 0
        for idx, (course, credit) in enumerate(courses, 1):
            print(f"{idx}. {course:<30} Credits: {credit}")
            total_credits += credit
        print("-"*50)
        print(f"Total courses enrolled:  {len(courses)}")
        print(f"Total credits:           {total_credits}")
        print("-"*50)
        return courses
    else:
        print("\nNo courses enrolled.")
        return []
