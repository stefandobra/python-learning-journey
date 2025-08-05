# def add_student(students: dict, name: str):
#     students[name] = []

# def print_student(students: dict, name: str):
#     if name not in students:
#         print(f"{name}: no such person in the database")
#     else: 
#         average = 0
#         sum_grades = 0
#         for course in students[name]:
#             sum_grades += course[1]
#         if len(students[name]) > 0:
#             average = sum_grades / len(students[name])

#         print(f"{name}:")
#         if len(students[name]) == 0:
#             print(" no completed courses")
#         else:
#             print(f" {len(students[name])} completed courses:")
#             for course in students[name]:
#                 print(f"  {course[0]} {course[1]}")
#             print(f" average grade {average}")

# def add_course(students: dict, name: str, course: tuple):
#     if course[1] == 0:
#         return
    
#     for value in students[name]:
#         if course[0] == value[0]:
#             if course[1] < value[1]:
#                 return
#             else:
#                 del students[name][0]

#     students[name].append((course[0], course[1]))
    
# def summary(students: dict):
#     student_no = 0
#     most_courses = [0, ""]
#     best_average = [0, ""]
#     average = 0
#     sum_grades = 0
#     for key, value in students.items():
#         student_no += 1
        
#         if len(value) > most_courses[0]:
#             most_courses = [len(value),key]
#         sum_grades = 0
#         for grade in value:    
#             sum_grades += grade[1]
#         if len(value) > 0:
#             average = sum_grades / len(value)   

#         if average > best_average[0]:
#             best_average = [average, key]   

#     print(f"students {student_no}")
#     print(f"most courses completed {most_courses[0]} {most_courses[1]}")
#     print(f"best average grade {best_average[0]} {best_average[1]}")
    

def add_student(students : dict, name: str):
    students[name] = {}

def print_student(students: dict, name: str):
    if name not in students:
        print(f"{name}: no such person in the database")
        return
    
    student_courses = students[name]

    print(f"{name}:")

    if len(student_courses) == 0:
        print(" no completed courses")
    else:
        print(f" {len(student_courses)} completed courses:")
        sum = 0
        for course, grade in student_courses.items():
            course_grade = grade[1]
            print(f"  {course} {course_grade}")
            sum += course_grade
        average = sum / len(student_courses)
        print(f" average grade {average:.1f}")

def add_course(students: dict, name: str, course: tuple):
    student_courses = students[name]

    course_name = course[0]
    course_grade = course[1]

    if course_grade == 0:
        return
    
    if course_name in student_courses:
        if student_courses[course_name][1] > course_grade:
            return
    
    student_courses[course_name] = course

def summary(students: dict):
    print(f"students {len(students)}")
    most_courses_count = 0
    best_average = 0

    for name, courses in students.items():
        if len(courses) > most_courses_count:
            most_courses = name
            most_courses_count = len(students[most_courses])
    
        sum = 0
        for course, grade in courses.items():
            sum += grade[1]

        if len(courses) > 0:
            average = sum / len(courses)
        else:
            average = 0
        
        if average > best_average:
            best_average = average
            best = name
    
    print(f"most courses completed {most_courses_count} {most_courses}")
    print(f"best average grade {best_average:.1f} {best}")









if __name__ == "__main__": 
    students = {}
    # add_student(students, "Peter")
    print_student(students, "Peter")
    # add_course(students, "Peter", ("Software Development Methods", 5))
    # summary(students)