# Developer's Reference Guide
## Smart Campus Information System

---

## 📖 Module Reference

### Q1: Student Registration (`student_registration.py`)

**Main Function:**
```python
def register_student_and_evaluate()
```

**Features:**
- Input validation for scores (0-100)
- Grade assignment using if-elif-else
- 5 performance levels
- Error handling for invalid input

**Grade Scale:**
- 90-100 → A (Excellent)
- 75-89 → B (Very Good)
- 60-74 → C (Good)
- 40-59 → D (Average)
- <40 → F (Needs Improvement)

**Return Value:** Dictionary with name, score, grade, remark

---

### Q2: Course Enrollment (`course_enrollment.py`)

**Main Function:**
```python
def manage_course_enrollment()
```

**Features:**
- While loop for repeated input
- Continue statement to skip invalid entries
- Break statement to enforce limits
- Validation for credits (1-10)
- Maximum 5 courses per student

**Data Structure:** List of tuples `[(course_name, credits), ...]`

**Return Value:** List of enrolled courses

---

### Q3: Student Records (`student_records.py`)

**Main Functions:**
```python
def manage_student_records()
def event_management(students)
```

**Data Structures:**
- **List:** Store multiple student records
- **Dictionary:** Individual student details
- **Sets:** Event participation tracking

**Set Operations Demonstrated:**
- Intersection: `&` (common elements)
- Union: `|` (all elements)
- Difference: `-` (exclusive elements)

**Return Value:** List of student dictionaries

---

### Q4: Search and Sort (`student_search_sort.py`)

**Sorting Functions:**
```python
def bubble_sort(arr)       # Compares adjacent elements
def selection_sort(arr)    # Finds minimum repeatedly
```

**Searching Functions:**
```python
def linear_search(arr, target)    # O(n) complexity
def binary_search(arr, target)    # O(log n) complexity - requires sorted array
```

**Time Complexity:**
- Bubble Sort: O(n²)
- Selection Sort: O(n²)
- Linear Search: O(n)
- Binary Search: O(log n)

---

### Q5: Fee Calculation (`fee_calculation.py`)

**Main Function:**
```python
def calculate_fee(tuition_fee, hostel_fee=0, transportation_fee=0)
```

**Features:**
- Default parameters for optional fees
- Interactive fee calculator
- Predefined examples

**Return Value:** Total fee (float)

---

### Q6: File Management (`file_management.py`)

**Main Function:**
```python
def manage_academic_records(base_path)
```

**Sub-functions:**
- `write_student_records()` - Write CSV data
- `read_student_records()` - Read from file
- `add_new_record()` - Append to file
- `generate_report_from_file()` - Process and analyze

**File Format:**
```
ID,Name,Marks
101,Student,Score
```

**Report Includes:**
- Total students
- Average marks
- Top student
- Detailed breakdown

---

### Q7: Directory Scanning (`directory_scanning.py`)

**Main Function:**
```python
def scan_directory(path)
```

**Exception Handling:**
```python
try:
    FileNotFoundError      # Invalid path
    NotADirectoryError     # Not a directory
    PermissionError        # Access denied
    MissingFileOrFolderError  # Custom exception (empty folder)
except:
    # Display user-friendly error
```

**Features:**
- Recursive directory traversal using `os.walk()`
- Folder hierarchy visualization
- Custom exception for empty folders

---

### Q8: Performance Analytics (`performance_analytics.py`)

**Main Function:**
```python
def analyze_student_performance(csv_filepath)
```

**Library Usage:**
- **Pandas:** Read CSV, statistical summaries
- **NumPy:** Mean, median, std deviation
- **Matplotlib:** Bar charts, line graphs

**Statistical Measures:**
```python
np.mean(scores, axis=0)      # Average
np.median(scores, axis=0)    # Median
np.std(scores, axis=0)       # Standard deviation
```

**Visualization:**
- Bar chart: Average scores per subject
- Bar chart: Student-wise performance

---

## 🔧 Code Organization

### Import Structure
```python
# In main.py
from modules.student_registration import register_student_and_evaluate
from modules.course_enrollment import manage_course_enrollment
# ... other imports
```

### Directory Structure
```
Python project/
├── main.py                  # Dashboard
├── modules/                 # All module implementations
│   └── *.py                 # Individual modules
├── Projects/                # Sample data
├── student_records.txt      # Data file
└── student_performance.csv  # Analytics data
```

---

## 🎯 Design Patterns

### 1. Modular Design
Each module is independent and can be:
- Tested separately
- Modified independently
- Reused in other projects
- Extended with new features

### 2. Menu-Driven Interface
```python
while True:
    display_menu()
    choice = input("Select option: ")
    execute_module(choice)
```

### 3. Input Validation
```python
try:
    value = float(input("Enter value: "))
    if value < 0 or value > 100:
        print("Invalid!")
        continue
except ValueError:
    print("Invalid input!")
    continue
```

### 4. Exception Handling
```python
try:
    # Operations that might fail
except SpecificError as e:
    # Handle specific error
except Exception as e:
    # Handle general error
```

---

## 📊 Data Flow

### Typical Module Flow
```
1. User Input
   ↓
2. Input Validation
   ↓
3. Process Data
   ↓
4. Display Output
   ↓
5. Return to Menu
```

### File-Based Module Flow
```
1. User Input
   ↓
2. Create/Open File
   ↓
3. Write/Read Data
   ↓
4. Process Data
   ↓
5. Generate Report
   ↓
6. Display Results
```

---

## 🧪 Testing Strategy

### Unit Testing (Individual Modules)
```python
# test_system.py
from modules.fee_calculation import calculate_fee
total = calculate_fee(50000, hostel_fee=30000, transportation_fee=10000)
assert total == 90000
```

### Integration Testing
- Test module imports
- Test function calls
- Test data flow
- Test file operations

### User Acceptance Testing
- Run examples.py
- Test interactive menu
- Test error handling
- Verify output formats

---

## 🔐 Error Handling Strategy

### Input Validation
```python
try:
    score = float(input("Enter score: "))
    assert 0 <= score <= 100
except ValueError:
    print("Invalid input")
except AssertionError:
    print("Score out of range")
```

### File Operations
```python
try:
    with open(filepath, "r") as f:
        data = f.readlines()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Access denied")
```

### Custom Exceptions
```python
class MissingFileOrFolderError(Exception):
    """Raised when required folder is missing"""
    pass

if condition:
    raise MissingFileOrFolderError("Error message")
```

---

## 📈 Performance Considerations

### Algorithm Efficiency
- **O(1):** Dictionary lookup, function call
- **O(n):** Linear search, list iteration
- **O(n²):** Bubble sort, selection sort
- **O(log n):** Binary search

### Optimization Tips
1. Use binary search for large datasets
2. Use dictionaries for O(1) lookups
3. Avoid nested loops where possible
4. Use sets for membership testing

---

## 🚀 Extending the System

### Adding a New Module

1. **Create module file:**
```python
# modules/new_module.py
def new_function():
    """Documentation"""
    pass
```

2. **Import in main.py:**
```python
from modules.new_module import new_function
```

3. **Add menu option:**
```python
elif choice == "Q11":
    self.run_new_module()
```

4. **Create handler method:**
```python
def run_new_module(self):
    try:
        new_function()
    except Exception as e:
        print(f"Error: {e}")
    input("Press Enter...")
```

---

## 📚 Code Examples

### Example 1: Using Lists and Dictionaries
```python
students = [
    {"name": "John", "age": 20, "grades": [85, 90]},
    {"name": "Jane", "age": 21, "grades": [92, 88]}
]

for student in students:
    avg = sum(student["grades"]) / len(student["grades"])
    print(f"{student['name']}: {avg:.1f}")
```

### Example 2: Using Sets
```python
event_A = {"Alice", "Bob", "Carol"}
event_B = {"Bob", "Carol", "Dave"}

common = event_A & event_B        # {'Bob', 'Carol'}
all_students = event_A | event_B  # {'Alice', 'Bob', 'Carol', 'Dave'}
only_A = event_A - event_B        # {'Alice'}
```

### Example 3: Sorting Algorithm
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```

### Example 4: File Operations
```python
# Write
with open("data.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")

# Read
with open("data.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line.rstrip())
```

---

## 🔍 Debugging Tips

1. **Print statements:** Add at key points
```python
print(f"DEBUG: variable = {variable}")
```

2. **Try-except blocks:** Catch and log errors
```python
try:
    # code
except Exception as e:
    print(f"Error: {e}")
```

3. **Input validation:** Check data immediately
```python
assert isinstance(value, (int, float)), "Must be numeric"
```

4. **Test modules independently:**
```python
if __name__ == "__main__":
    test_function()
```

---

## 📝 Documentation Best Practices

### Function Documentation
```python
def calculate_fee(tuition_fee, hostel_fee=0, transportation_fee=0):
    """
    Calculate total student fee.
    
    Args:
        tuition_fee (float): Required tuition fee
        hostel_fee (float, optional): Hostel fee (default 0)
        transportation_fee (float, optional): Transport fee (default 0)
    
    Returns:
        float: Total fee amount
    """
```

### Inline Comments
```python
# Initialize counters
total = 0
count = 0

# Process each record
for record in records:
    # Skip empty records
    if not record:
        continue
    total += record['amount']
    count += 1
```

---

## 🎓 Learning Resources

### Python Concepts Covered
1. **Basic Syntax:** Variables, operators, data types
2. **Control Flow:** if-elif-else, while, for loops
3. **Functions:** Parameters, defaults, return values
4. **Data Structures:** Lists, dictionaries, sets, tuples
5. **File I/O:** Read, write, append operations
6. **Exception Handling:** try-except-finally, custom exceptions
7. **Libraries:** NumPy, Pandas, Matplotlib
8. **Algorithms:** Sorting, searching, set operations

### Recommended Next Topics
1. Object-oriented programming (classes, inheritance)
2. Database integration (SQLite, MySQL)
3. Web development (Flask, Django)
4. Advanced data analysis (scikit-learn, scipy)
5. API development (REST, GraphQL)

---

## ✅ Checklist for Module Development

- [ ] Function signature defined
- [ ] Input validation implemented
- [ ] Exception handling added
- [ ] Return values specified
- [ ] Documentation written
- [ ] Test cases created
- [ ] Integration tested
- [ ] Menu option added
- [ ] Error messages user-friendly
- [ ] Code follows conventions

---

## 🎯 Performance Optimization Checklist

- [ ] Remove unnecessary loops
- [ ] Use appropriate data structures
- [ ] Cache repeated calculations
- [ ] Optimize file I/O operations
- [ ] Profile code for bottlenecks
- [ ] Use efficient algorithms
- [ ] Minimize memory usage

---

**This guide provides everything needed to understand, modify, and extend the Smart Campus Information System.**
