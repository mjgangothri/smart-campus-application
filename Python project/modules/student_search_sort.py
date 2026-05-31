# Q4: Sorting and Searching of Student IDs
def sorting_and_searching_demo():
    """
    Demonstrates sorting and searching algorithms
    """
    print("\n" + "="*50)
    print("    SORTING AND SEARCHING STUDENT IDS")
    print("="*50)
    
    # Step 1: Get student IDs from user or use default
    print("\nOption 1: Use default student IDs")
    print("Option 2: Enter custom student IDs")
    
    choice = input("\nSelect option (1/2): ").strip()
    
    if choice == "2":
        try:
            ids_input = input("Enter student IDs (comma-separated): ").strip()
            student_ids = [int(id.strip()) for id in ids_input.split(",")]
            if not student_ids:
                print("No IDs entered. Using default IDs.")
                student_ids = [105, 102, 110, 108, 101, 115]
        except ValueError:
            print("Invalid input! Using default IDs.")
            student_ids = [105, 102, 110, 108, 101, 115]
    else:
        student_ids = [105, 102, 110, 108, 101, 115]
    
    print(f"\nOriginal IDs: {student_ids}")
    
    # Step 2: Bubble Sort
    print("\n" + "-"*50)
    print("            BUBBLE SORT")
    print("-"*50)
    sorted_ids_bubble = bubble_sort(student_ids.copy())
    print(f"Sorted IDs (Bubble Sort): {sorted_ids_bubble}")
    
    # Step 3: Selection Sort
    print("\n" + "-"*50)
    print("            SELECTION SORT")
    print("-"*50)
    sorted_ids_selection = selection_sort(student_ids.copy())
    print(f"Sorted IDs (Selection Sort): {sorted_ids_selection}")
    
    # Step 4 & 5: Search Operations
    print("\n" + "-"*50)
    print("            SEARCH OPERATIONS")
    print("-"*50)
    
    try:
        target = int(input("\nEnter student ID to search: "))
        
        # Linear Search
        linear_result = linear_search(sorted_ids_bubble, target)
        if linear_result != -1:
            print(f"✓ Linear Search: ID {target} found at index {linear_result}")
        else:
            print(f"✗ Linear Search: ID {target} not found")
        
        # Binary Search
        binary_result = binary_search(sorted_ids_bubble, target)
        if binary_result != -1:
            print(f"✓ Binary Search: ID {target} found at index {binary_result}")
        else:
            print(f"✗ Binary Search: ID {target} not found")
            
    except ValueError:
        print("Invalid input! Please enter a valid ID.")
    
    print("-"*50)


def bubble_sort(arr):
    """Bubble Sort Algorithm"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def selection_sort(arr):
    """Selection Sort Algorithm"""
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def linear_search(arr, target):
    """Linear Search Algorithm"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    """Binary Search Algorithm (requires sorted array)"""
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1
