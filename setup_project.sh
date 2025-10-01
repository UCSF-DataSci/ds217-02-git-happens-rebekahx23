#!/bin/bash

mkdir -p src data output
echo "Project structure created with src, data, and output directories."

touch .gitignore
touch requirements.txt src/data_analysis.py src/data_analysis_functions.py
echo "Created .gitignore and requirements.txt files."

touch data/courses.json

cat > data/students.csv << 'EOF'
name,age,grade,subject
Alice,20,85,Math
Bob,19,92,Science
Charlie,21,78,English
Diana,20,88,Math
Eve,22,95,Science
Frank,19,82,History
Grace,21,91,Math
Henry,20,76,Science
EOF
echo "Sample students.csv file created in the current directory."

cat > src/data_analysis.py << 'EOF'
def load_students(filename):
    # TODO: Read CSV and return list of student data
    return

def calculate_average_grade(students): 
    # TODO: Calculate and return average
    return 

def count_math_students(students):
    # TODO: Count students in Math
    return

def generate_report():
    # TODO: Create formatted report string
    return

def save_report(report, filename):
    # TODO: Write report to file
    return

def main():
    # TODO: Orchestrate the analysis
    return
EOF
echo "Created src/data_analysis.py with function stubs and TODO comments."

cat > src/data_analysis_functions.py << 'EOF'
def load_data(filename):
    # TODO: Generic loader that checks file extension
    return

def load_csv(filename):
    # TODO: Load CSV data (same technique as basic script)
    return

def analyze_data(students):
    # TODO: Return dictionary with multiple statistics
    return

def analyze_grade_distribution(grades):
    # TODO: Count grades by letter grade ranges
    return

def save_results(results, filename):
    # TODO: Save detailed report
    return

def main():
    # TODO: Orchestrate the analysis using all functions
    return
EOF
echo "Created src/data_analysis_functions.py with function stubs and TODO comments."




