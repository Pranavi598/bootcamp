def calculate_score(marks):
    return sum(marks) / len(marks)

def main():
    student_marks = [80, 90, 85]
    print("Average score:", calculate_score(student_marks))

if __name__ == "__main__":
    main()
