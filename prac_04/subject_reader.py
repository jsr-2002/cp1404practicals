def main():
    """Read data from file and display formatted subject details."""
    subjects = load_subjects()
    display_subjects(subjects)


def load_subjects():
    """Load subject data from subject_data.txt and return as list of lists."""
    subjects = []
    with open("subject_data.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            parts[2] = int(parts[2])  # convert student number to int
            subjects.append(parts)
    return subjects


def display_subjects(subjects):
    """Display each subject with formatted details."""
    for subject in subjects:
        code, lecturer, students = subject
        print(f"{code} is taught by {lecturer} and has {students} students")


main()
