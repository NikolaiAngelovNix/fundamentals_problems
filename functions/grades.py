def grade(gr):
    if 0 <= gr <= 2.99:
        print("Fail")
    elif 3 <= gr <= 3.49:
        print("Poor")
    elif 3.5 <= gr <= 4.49:
        print("Good")
    elif 4.5 <= gr <= 5.49:
        print("Very Good")
    elif 5.5 <= gr <= 6:
        print("Excellent")


input_grade = float(input())
grade(input_grade)
