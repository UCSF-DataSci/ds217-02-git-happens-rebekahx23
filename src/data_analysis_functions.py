from data_analysis import calculate_average_grade, generate_report, get_grades_list, save_report


def load_data(filename):
    # TODO: Generic loader that checks file extension
    # case-insensitive
    is_csv = filename.lower().endswith('.csv')
    if is_csv:
        students = load_csv(filename)
    
    if not is_csv:
        print("No data loaded. Please check filename")
        return

    print(f"Loaded {len(students)} students")
    return

def load_csv(filename):
    # TODO: Load CSV data (same technique as basic script)
    students = []
    try:
        with open(filename, 'r') as file:
            reader = students.DictReader(filename)
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

def find_highest_grade(grades):
    """Find the highest grade in a list."""
    if not grades:
        return 0
    return max(grades)

def lowest_grade(grades):
    """Find the lowest grade in a list."""
    lowest = min(grades) if grades else 0
    if not grades:
        return 0
    return lowest

def get_total_students(students):
    """Get total number of students."""
    return len(students)

def analyze_data(students):
    # TODO: Return dictionary with multiple statistics
    grades = get_grades_list(students)
    average = calculate_average_grade(students)
    highest = find_highest_grade(grades)
    total_students = get_total_students(students)
    lowest = lowest_grade(grades)
    
    return {
        'total_students': total_students,
        'average_grade': average,
        'highest_grade': highest,
        'lowest_grade': lowest
    }

def analyze_grade_distribution(grades):
    # TODO: Count grades by letter grade ranges
    """Analyze the distribution of grades."""
    if not grades:
        return {}

    # Count grades by ranges
    distribution = {
        'A (90-100)': 0,
        'B (80-89)': 0,
        'C (70-79)': 0,
        'D (60-69)': 0,
        'F (0-59)': 0
    }

    for grade in grades:
        if grade >= 90:
            distribution['A (90-100)'] += 1
        elif grade >= 80:
            distribution['B (80-89)'] += 1
        elif grade >= 70:
            distribution['C (70-79)'] += 1
        elif grade >= 60:
            distribution['D (60-69)'] += 1
        else:
            distribution['F (0-59)'] += 1

    return distribution

def save_results(results, filename):
    # TODO: Save detailed report
    
    save = save_report(results, filename)
    return

def main():
    # TODO: Orchestrate the analysis using all functions
    students = load_data('data/students.csv')
    print(calculate_average_grade(students))
    if not students:
        print("No student data to analyze")
        return

    # Calculate statistics
    grades_avg = calculate_average_grade(students)
    total = len(students)
    data = analyze_data(students)
    results = generate_report(
            data['total_students'],
            data['average_grade'],
            data['highest_grade']
        )
    
    save_results(results, 'output/analysis_report.txt')
    return
