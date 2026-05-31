# Q5: Student Fee Calculation using Functions
def calculate_fee(tuition_fee, hostel_fee=0, transportation_fee=0):
    """
    Calculates total fee for a student
    
    Parameters:
    - tuition_fee: Required tuition fee
    - hostel_fee: Optional hostel fee (default 0)
    - transportation_fee: Optional transportation fee (default 0)
    
    Returns:
    - Total fee amount
    """
    total_fee = tuition_fee + hostel_fee + transportation_fee
    return total_fee


def manage_student_fees():
    """
    Interactive fee calculation module
    """
    print("\n" + "="*50)
    print("    STUDENT FEE CALCULATION")
    print("="*50)
    
    try:
        # Get tuition fee
        tuition = float(input("\nEnter tuition fee: "))
        if tuition < 0:
            print("Fee cannot be negative!")
            return
        
        # Ask if hostel fee applies
        has_hostel = input("Include hostel fee? (y/n): ").strip().lower()
        hostel = 0
        if has_hostel == 'y':
            hostel = float(input("Enter hostel fee: "))
            if hostel < 0:
                print("Fee cannot be negative!")
                return
        
        # Ask if transportation fee applies
        has_transport = input("Include transportation fee? (y/n): ").strip().lower()
        transport = 0
        if has_transport == 'y':
            transport = float(input("Enter transportation fee: "))
            if transport < 0:
                print("Fee cannot be negative!")
                return
        
        # Calculate total fee
        total = calculate_fee(tuition, hostel_fee=hostel, transportation_fee=transport)
        
        # Display fee breakdown
        print("\n" + "-"*50)
        print("            FEE BREAKDOWN")
        print("-"*50)
        print(f"Tuition Fee:           ₹ {tuition:,.2f}")
        if hostel > 0:
            print(f"Hostel Fee:            ₹ {hostel:,.2f}")
        if transport > 0:
            print(f"Transportation Fee:    ₹ {transport:,.2f}")
        print("-"*50)
        print(f"TOTAL FEE:             ₹ {total:,.2f}")
        print("-"*50)
        
        return total
        
    except ValueError:
        print("Invalid input! Please enter valid fee amounts.")
        return None


def predefined_fee_examples():
    """
    Demonstrates fee calculation with predefined examples
    """
    print("\n" + "="*50)
    print("    PREDEFINED FEE CALCULATION EXAMPLES")
    print("="*50)
    
    # Case 1: Only tuition fee
    tuition = 50000
    total1 = calculate_fee(tuition)
    print(f"\nCase 1 - Tuition only: ₹ {total1:,}")
    
    # Case 2: Tuition + Hostel
    tuition = 50000
    hostel = 30000
    total2 = calculate_fee(tuition, hostel_fee=hostel)
    print(f"Case 2 - Tuition + Hostel: ₹ {total2:,}")
    
    # Case 3: Tuition + Hostel + Transportation
    tuition = 50000
    hostel = 30000
    transport = 10000
    total3 = calculate_fee(tuition, hostel_fee=hostel, transportation_fee=transport)
    print(f"Case 3 - Tuition + Hostel + Transport: ₹ {total3:,}")
    
    print("-"*50)
