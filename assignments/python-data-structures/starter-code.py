# Python Data Structures Starter Code

# Task 1

def average_score(scores):
    """Return the average value from a list of numeric scores."""
    pass


def top_three_students(students):
    """Return the names of the top three students by score."""
    pass

# Task 2

def find_student_grade(students, name):
    """Return the grade for the given student name, or 'Not found'."""
    pass


def class_summary(students):
    """Return summary statistics for the class data."""
    pass

# Task 3

def filter_passing(scores):
    """Return a list of scores that are 60 or higher."""
    pass


def scale_scores(scores, factor):
    """Return a new list with each score multiplied by factor."""
    pass


if __name__ == "__main__":
    example_scores = [82, 95, 58, 74, 90]
    example_students = {
        "Amina": 88,
        "Diego": 74,
        "Lina": 95,
        "Noah": 63,
        "Zoe": 78,
    }

    print("Average score:", average_score(example_scores))
    print("Top three students:", top_three_students(example_students))
    print("Lina's grade:", find_student_grade(example_students, "Lina"))
    print("Class summary:", class_summary(example_students))
    print("Passing scores:", filter_passing(example_scores))
    print("Scaled scores:", scale_scores(example_scores, 1.1))
