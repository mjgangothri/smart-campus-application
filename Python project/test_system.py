#!/usr/bin/env python3
"""
Test script to verify all modules load correctly
"""

import sys
import os

print("="*60)
print("Smart Campus Information System - Module Test")
print("="*60)

print(f"\nPython Version: {sys.version}")
print(f"Working Directory: {os.getcwd()}")

print("\nTesting module imports...")
print("-"*60)

try:
    print("✓ Importing student_registration...")
    from modules.student_registration import register_student_and_evaluate
    
    print("✓ Importing course_enrollment...")
    from modules.course_enrollment import manage_course_enrollment
    
    print("✓ Importing student_records...")
    from modules.student_records import manage_student_records
    
    print("✓ Importing student_search_sort...")
    from modules.student_search_sort import sorting_and_searching_demo
    
    print("✓ Importing fee_calculation...")
    from modules.fee_calculation import calculate_fee, manage_student_fees
    
    print("✓ Importing file_management...")
    from modules.file_management import manage_academic_records
    
    print("✓ Importing directory_scanning...")
    from modules.directory_scanning import scan_directory
    
    print("✓ Importing performance_analytics...")
    from modules.performance_analytics import analyze_student_performance
    
    print("\n" + "-"*60)
    print("✅ ALL MODULES LOADED SUCCESSFULLY!")
    print("-"*60)
    
    # Test basic functionality
    print("\nTesting basic functionality...")
    print("-"*60)
    
    # Test fee calculation
    print("✓ Testing fee calculation function...")
    total = calculate_fee(50000, hostel_fee=30000, transportation_fee=10000)
    assert total == 90000, f"Fee calculation failed: expected 90000, got {total}"
    print(f"  Total fee calculated: ₹ {total:,}")
    
    # Test sorting functions
    print("✓ Testing sorting and search functions...")
    from modules.student_search_sort import bubble_sort, linear_search
    test_ids = [105, 102, 110, 108]
    sorted_ids = bubble_sort(test_ids.copy())
    assert sorted_ids == [102, 105, 108, 110], "Bubble sort failed"
    result = linear_search(sorted_ids, 108)
    assert result == 2, f"Linear search failed: expected 2, got {result}"
    print(f"  Sorting and search algorithms working correctly")
    print("\n" + "="*60)
    print("✅ SYSTEM TEST PASSED - READY TO USE!")
    print("="*60)
    print("\nTo start the system, run: python main.py")
    
except ImportError as e:
    print(f"\n❌ Import Error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"\n❌ Test Error: {e}")
    sys.exit(1)
