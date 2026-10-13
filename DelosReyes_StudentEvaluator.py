
name = input("What is your name?")
assessment_1 = float(input("What is your assessment 1 score? "))
assessment_2 = float(input("What is your assessment 2 score? "))
assessment_3 = float(input("What is your assessment 3 score? "))
average = (assessment_1 + assessment_2 + assessment_3)/ 3


def display_header():
    print("================================")
    print("Student Performance Evaluation")
    print("================================")

def get_student_info():
    print(name)
    print(assessment_1, assessment_2, assessment_3)

def evaluate_performance():
    print(f"Average: {average:.2f}")


    if average >= 90:
        print("Oustanding!")
    elif average >= 85:
        print("Very Satisfactory!")
    elif average >= 80:
        print("Satisfactory!")
    elif average >= 75:
        print("Fairly Satisfactory!")
    elif average < 75:
        print("Needs Improvement")


def display_performance():
    get_student_info()
    evaluate_performance()
display_header()
display_performance()


