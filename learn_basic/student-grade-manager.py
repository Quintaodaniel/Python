"""
Project: Student Grade Manager

Skills practiced:
- Functions and return values
- Loops (while, for)
- Conditional logic (if/elif/else)
- Input validation and error handling
- List and dictionary manipulation
- String methods (strip)
- Nested data structures
- Aggregating data for statistics
"""


def get_student_name():
    name = input("Enter student name (or press Enter to finish): ").strip()
    return name


def get_student_grades():
    grades = []
    while True:
        try:
            grade_input = input("Enter a grade between 0 and 100 (or press Enter to finish): ").strip()
            if grade_input == "":
                if grades:
                    break
                else:
                    print("Enter at least one grade.")
                    continue
            grade = float(grade_input)
            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric grade.")
    return grades

def calculate_average(grades):
    return sum(grades) / len(grades)

def classify_student(avg):
    if avg >= 70:
        return "Approved"
    elif 50 <= avg < 70:
        return "Recovery"
    else:
        return "Failed"

def show_statistics(all_grades):
    all_flat = [grade for grades in all_grades.values() for grade in grades]
    if not all_flat:
        print("No grades to show statistics.")
        return
    print("\nGeneral Statistics:")
    print(f"Highest grade: {max(all_flat):.2f}")
    print(f"Lowest grade: {min(all_flat):.2f}")
    print(f"Average grade: {sum(all_flat) / len(all_flat):.2f}")

def main():
    student_grades = {}
    while True:
        name = get_student_name()
        if name == "":
            break
        grades = get_student_grades()
        student_grades[name] = grades

    if not student_grades:
        print("No students entered.")
        return

    print("\nStudent Results:")
    for name, grades in student_grades.items():
        avg = calculate_average(grades)
        status = classify_student(avg)
        print(f"{name}: Average = {avg:.2f}, Status = {status}")

    show_statistics(student_grades)

if __name__ == "__main__":
    main()
