import csv

def load_students(filename):
    # TODO: Read CSV and return list of student data
    """Load student data from CSV file."""
    students = []
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({
                    'name': row['name'],
                    'age': int(row['age']),
                    'grade': int(row['grade']),
                    'subject': row['subject']
                })
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
    except Exception as e:
        print(f"Error loading data: {e}")

    return students

def get_grades_list(students):
    """Extract grades from student list."""
    return [student['grade'] for student in students]

def calculate_average_grade(students): 
    grades = get_grades_list(students)
    if not students:
        return 0
    return sum(grades) / len(grades)


def count_math_students(students):
    # TODO: Count students in Math
    count = 0
    for student in students:
        if student['subject'] == 'Math':
            count += 1
    return  count

def generate_report(total, average, math_count):
    """Generate report string."""
    # TODO: Create formatted string with results
    # TODO: Use f-strings with .1f for decimals
    report = (
        "Student Grade Analysis\n"
        "=======================\n\n"
        "Individual Grades:\n\n"
        "Summary:\n"
        f"Total Students: {total}\n"
        f"Average Grade: {average:.1f}\n"
        f"Math Students: {math_count}"
    )
    return report

def save_report(report, filename):
    """Save report to file."""
    # TODO: Create output directory if needed
    # TODO: Write report to file
    """Save analysis results to a file."""
    try:
        with open(filename, 'w') as file:
            file.write(report)
   
        print(f"Results saved to {filename}")
        return True
    except Exception as e:
        print(f"Error saving file: {e}")
        return False

def main():
    students = load_students('data/students.csv')
    print(calculate_average_grade(students))
    if not students:
        print("No student data to analyze")
        return

    # Calculate statistics
    grades_avg = calculate_average_grade(students)
    total = len(students)
    math_count = count_math_students(students)

    # Save results
    output_file = 'output/analysis_report.txt'
    print(load_students('data/students.csv'))
    save_report(generate_report(total, grades_avg, math_count), output_file)

if __name__ == "__main__":
    main()