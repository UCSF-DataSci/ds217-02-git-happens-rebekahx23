from data_analysis import calculate_average_grade, get_grades_list, load_students, save_report


def load_data(filename):
    # TODO: Generic loader that checks file extension
    # case-insensitive
    is_csv = filename.lower().endswith('.csv')
    if is_csv:
        students = load_csv(filename)
        print(f"Loaded {len(students)} students")
        return students
    else:
        print("No data loaded. Please check filename")

def load_csv(filename):
    # TODO: Load CSV data (same technique as basic script)
    return load_students(filename)

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
    
    save_report(results, filename)
    return

def generate_report(statistics):
    """Generate report string."""
    # TODO: Create formatted string with results
    # TODO: Use f-strings with .1f for decimals
    report = (
        "Student Grade Analysis\n"
        "=======================\n\n"
        "Individual Grades:\n\n"
        "Summary:\n"
        f"Total Students: {statistics['total_students']}\n"
        f"Average Grade: {statistics['average_grade']:.1f}\n"
        f"Highest Grade: {statistics['highest_grade']:.1f}\n"
        f"Lowest Grade: {statistics['lowest_grade']:.1f}\n"
    )
    return report

def main():
    # TODO: Orchestrate the analysis using all functions
    students = load_data('data/students.csv')
    if not students:
        print("No student data to analyze")
        return

    # Calculate statistics
    data = analyze_data(students)
    results = generate_report(statistics=data)
    
    save_results(results, 'output/analysis_report.txt')
    return

if __name__ == "__main__":
    main()